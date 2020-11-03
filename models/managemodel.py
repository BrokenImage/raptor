## This file is the main file for the manage model CLI for training anb uploading models to a model registry ###
import os
import click
import boto3
from dotenv import load_dotenv
from pymongo import MongoClient
from utils.ClickClasses import LiteralOption
from utils.ModelRegistry import ModelRegistry
from utils.create_dataset import create_dataset_json, create_dataset_mongo
load_dotenv()


@click.group()
def cli():
    pass

@cli.command()
@click.option('--access-key-id', '-id', help='the access key for s3 created in your AWS account\'s security credentials')
@click.option('--secret-key', '-key', help='the seceret key for s3 created in your AWS accoun\'s security credentials')
@click.option('--bucket-name', '-bucket', help='the bucket/access point url for your aws bucket')
@click.option('--mongo-url', '-db', help='the mongodb client url for where the model registry')
def setup_registry(access_key_id, secret_key, bucket_name, mongo_url):
    """Setup the cli's connected to the model registry"""

    access_key_id = click.prompt("Please enter your s3 iam user access token", default=access_key_id)
    secret_key = click.prompt("Please enter your s3 iam user secret key", default=secret_key)
    bucket_name = click.prompt("Please enter your s3 bucker name", default=bucket_name)
    mongo_url = click.prompt("Please enter the mongodb client url", default=mongo_url)

    os.environ['AWS_ACCESS_KEY_ID'] = access_key_id
    os.environ['AWS_SECRET_KEY'] = secret_key
    os.environ['AWS_BUCKET_NAME'] = bucket_name
    os.environ['MONGO_CLIENT_URL'] = mongo_url


@cli.command()
@click.argument('file_name', type=click.Path(exists=True), required=True)
@click.option('--input_type', type=str, default='json', help='the type of input the command should use (defualt mongo)')
@click.option('--size', type=int, default=0, help='the size of the dataset (defualt max)')
@click.option('--classes', cls=LiteralOption, default=[], help='the classes that should be in the dataset (default all)')
@click.option('--test_size', type=int, default=0.25, help='the percentage of the data that should be split into training data (default 25%)')
@click.option('--add_to', type=click.Path(exists=True), default='', help='the path to a csv file to add the new data too')
def create_dataset(file_name, input_type, size, classes, test_size, add_to):
    """Creates a dataset for training an anomoly ML model"""
    if input_type == 'mongo':
        create_dataset_mongo(file_name, size, classes, test_size, add_to)
    elif input_type == 'json':
        create_dataset_json(file_name, size, classes, test_size, add_to)
    else:
        click.BadParameter('Invalid input type given, choose either mongo or json')


@cli.command()
@click.argument('model_path', type=click.Path(exists=True))
@click.argument('classes_path', type=click.Path(exists=True))
@click.argument('name', type=str)
@click.argument('metrics', type=str)
@click.option('--increment-version', is_flag=True, 
    help='if set, will increment version from an already existing model in the registry with the same name')
def upload_model(model_path, classes_path, name, metrics, increment_version):
    """Uploads a model document to the model registry"""
    session = boto3.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
        aws_secret_access_key=os.environ['AWS_SECRET_KEY']
    )
    registry = ModelRegistry(
        MongoClient(os.environ['MONGO_CLIENT_URL']).registry, 
        session.resource('s3'), 
        bucket_name=os.environ['AWS_BUCKET_NAME']
    )

    if increment_version:
        registry.increment_version(model_path, classes_path, name, metrics)
    else:
        registry.publish_model(model_path, classes_path, name, metrics)


@cli.command()
@click.argument('model_name', type=str)
@click.argument('model_version', type=int)
@click.option('--stage', type=click.Choice(['DEVELOPMENT', 'PRODUCTION'], case_sensitive=True), 
        help='the stage of the model, DEVELOPMENT or PRODUCTION', default='PRODUCTION')
def update_stage(model_name, model_version, stage):
    """Updates the stage of the model with the given name and version"""
    session = boto3.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
        aws_secret_access_key=os.environ['AWS_SECRET_KEY']
    )
    registry = ModelRegistry(
        MongoClient(os.environ['MONGO_CLIENT_URL']).registry, 
        session.resource('s3'), 
        bucket_name=os.environ['AWS_BUCKET_NAME']
    )
    registry.update_stage(model_name, model_version, stage)



if __name__ == '__main__':
    cli()