import os
import boto3
import numpy as np
import tensorflow as tf
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from werkzeug.datastructures import FileStorage
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_restplus import Api, Resource
from utils.Model import ModelManager
load_dotenv()

# Mongodb connection
client = MongoClient(os.environ['MONGO_CLIENT_URL'])
db = client.registry

# AWS S3 connection
session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_KEY']
)
s3 = session.resource('s3')

# App and API setup
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version="1.0", title="Anomaly Detection", description="")
ns = api.namespace('api')
single_parser = api.parser()
single_parser.add_argument("files", location="files", type=FileStorage, action='append', required=True)

graph = tf.get_default_graph()
backup_model = load_model("./models/backup/model.h5") 
backup_label_encoder = LabelEncoder()
backup_label_encoder.classes_ = np.load("./models/backup/classes.npy")

@ns.route("/classify")
class MultiClassification(Resource):
    @api.doc(parser=single_parser, description='Upload an image of a solar panel')
    def post(self):
        model = ModelManager(db, s3, graph, backup_model, backup_label_encoder,
            bucket_name=os.environ['AWS_BUCKET_NAME'])
        model.load_latest_model()
        
        args = single_parser.parse_args()
        image_files = args.files

        preds = []
        for image in image_files:
            image_array = model.preprocess(image)
            preds.append(model.predict(image_array)[0])

        return {'prediction': str(preds)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
