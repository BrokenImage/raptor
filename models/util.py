# from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from functools import reduce
import pandas as pd
import json
import os

# # MongoDb Client
# client = MongoClient()
# db = client.raptor 
# images = db.images 

def create_dataset_mongo(file_name, dataset_size=0, anomalies=[], test_size=0.25, complement=''):
    """Creates a new csv file to be used to train a anomaly detection model or adds data
        to an existing csv file by creating a dataframe and the combining them.
        Params:
            name (str): 
                The file name for the csv file. (required)
            dataset_size (int): 
                The total number of images that the dataset should contain. if set to zero
                it will get all the images of a the specified types in the collection. (default 0)
            anomalies ([str]):
                The anomaly classes that are to be added to the dataset. (default all)
            test_size (float or int):
                The percent of the data that will be used for train data. (default all)
    """
    if not anomalies:
        anomalies = images.distinct('anomaly')

    anom_images = [images.find( { 'anomaly': anomaly } ) for anomaly in anomalies]
    anom_images.sort(key=len)

    total_images = reduce(lambda x,y: len(x)+len(y), anom_images)
    anaomaly_split = total_images // len(anomalies)

    # Calculate how many of each anomaly type should be added the the dataset
    anom_counts = []
    for index, anomaly_lst in enumerate(anom_images):
        n = len(anomaly_lst)
        if n < anaomaly_split:
            remaining_counts = anom_counts[index:]
            for i in remaining_counts:
                anomaly_counts[i] += (anaomaly_split - n) // len(remaining_counts)

    image_docs = [anom_images[i][:anom_counts[i]] for i in range(len(anomalies))]
    keys = [key for key in images.findOne()]

    # Format data to be converted into csv file
    data = {key:[doc[key] for doc in image_docs] for key in keys}

    # Create a dataframe from the formated data
    df = pd.Dataframe(data, columns=keys)
    if complement != '':
        df = pd.merge(df, pd.read_csv(complement), how='outer', on='x1')

    # TODO: Use train test split to evenly split the dataset into train and test

    # Save the dataframe as a csv file
    df.to_csv(file_name)



def create_dataset_json(file_name, dataset_size=0, anomalies=[], test_size=0.25, complement=''):
    """Creates a new csv file to be used to train a anomaly detection model or adds data
        to an existing csv file by creating a dataframe and the combining them.
        Params:
            name (str): 
                The file name for the csv file. (required)
            dataset_size (int): 
                The total number of images that the dataset should contain. if set to zero
                it will get all the images of a the specified types in the collection. (default 0)
            anomalies ([str]):
                The anomaly classes that are to be added to the dataset. (default all)
            test_size (float or int):
                The percent of the data that will be used for train data. (default all)
    """
    with open('module_metadata.json') as f:
        image_dict = json.load(f)
    image_nums = image_dict.keys()

    if not anomalies:
        anomalies = get_distinct_anomalies(image_dict, image_nums)

    anom_images = [find_anomaly(anomaly, image_dict, image_nums) for anomaly in anomalies]
    anom_images.sort(key=len)

    total_images = reduce(lambda x,y: x+len(y), anom_images, 0)
    anaomaly_split = total_images // len(anomalies)

    # Calculate how many of each anomaly type should be added the the dataset
    anom_counts = [anaomaly_split] * len(anomalies)
    for index, anomaly_lst in enumerate(anom_images):
        n = len(anomaly_lst)
        if n < anaomaly_split:
            remaining_counts = anom_counts[index:]
            for i in range(len(remaining_counts)):
                anom_counts[i] += (anaomaly_split - n) // len(remaining_counts)

    image_doc_nums = [anom_images[i][:anom_counts[i]] for i in range(len(anomalies))]
    image_docs = []
    for anomaly_nums in image_doc_nums:
        for num in anomaly_nums:
            image_docs.append(image_dict[num])
    keys = image_dict["1"].keys()

    # Format data to be converted into csv file
    data = {key:[doc[key] for doc in image_docs] for key in keys}

    # Create a dataframe from the formated data
    df = pd.DataFrame(data, columns=keys)
    if complement != '':
        df = pd.merge(df, pd.read_csv(complement), how='outer', on='x1')

    # TODO: Use train test split to evenly split the dataset into train and test

    # Save the dataframe as a csv file
    df.to_csv(file_name)

def get_distinct_anomalies(image_dict, image_nums):
    distinct_anomalies = []
    for num in image_nums:
        if image_dict[num]['anomaly_class'] not in distinct_anomalies:
            distinct_anomalies.append(image_dict[num]['anomaly_class'])
    return distinct_anomalies

def find_anomaly(anomaly, image_dict, image_nums):
    anomaly_nums = []
    for num in image_nums:
        if image_dict[num]['anomaly_class'] == anomaly:
            anomaly_nums.append(num)
    return anomaly_nums


if __name__ == '__main__':
    create_dataset_json('test.csv', 50, anomalies=['Diode-Multi'])