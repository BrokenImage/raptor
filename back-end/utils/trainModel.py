import numpy as np
import keras as k
import tensorflow as tf
import json
import os
import boto3
from pymongo import MongoClient
from modelManager import ModelManager
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from sklearn.model_selection import train_test_split
from keras.regularizers import l2

def preprocess_images_labels(images_paths, category):
    X_train, X_test, y_train, y_test = train_test_split(images_paths, category, test_size=0.2)
    labelencoder = LabelEncoder()
    labelencoder.classes_ = np.load("./models/backup/classes.npy")
    y_train = labelencoder.fit_transform(y_train) # encode labels to numbers
    y_test = labelencoder.transform(y_test)
    y_train = k.utils.to_categorical(y_train) # encode nubers to catagorical labels
    y_test = k.utils.to_categorical(y_test)
    return X_train, X_test, y_train, y_test

def preprocess(image):
    image = image.reshape(40, 24, 1)
    return image / 255

def imageLoader(files, categories, batch_size):
    total_images = len(files)
    while True:
        batch_start = 0
        batch_end = batch_size

        while batch_start < total_images:
            limit = min(batch_end, total_images)
            X = [preprocess(np.array(load_img(image_path, color_mode = "grayscale"))) for image_path in files[batch_start:limit]]
            Y = categories[batch_start:limit]

            yield (np.array(X), np.array(Y)) # a tuple with two numpy arrays with batch_size samples     

            batch_start += batch_size   
            batch_end += batch_size

def define_model():
    """
    This model is a little less accurate than the best one I found.
    But it also has onlya quarter the paramenters so its a lot smaller.
    """
    model = k.Sequential()
    model.add(k.layers.Conv2D(filters=15, kernel_size=(3,3), strides=(1, 1), padding="valid", input_shape=(40, 24, 1), kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
    model.add(k.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2), padding="same"))
    model.add(k.layers.Conv2D(filters=15, kernel_size=(3,3), strides=(1, 1), padding="valid", kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
    model.add(k.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2), padding="same"))
    model.add(k.layers.Flatten())
    model.add(k.layers.Dense(675))
    model.add(k.layers.Activation('relu'))
    model.add(k.layers.Dense(11))
    model.add(k.layers.Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    model.summary()
    return model


# Mongodb connection
client = MongoClient(os.environ['MONGO_CLIENT_URL'])
db = client.registry

# AWS S3 connection
session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_KEY']
)
s3 = session.resource('s3')

graph = tf.get_default_graph()
backup_model = load_model("./models/backup/model.h5") 
backup_label_encoder = LabelEncoder()
backup_label_encoder.classes_ = np.load("./models/backup/classes.npy")

model = ModelManager(db, s3, graph, backup_model, backup_label_encoder,
        bucket_name=os.environ['AWS_BUCKET_NAME'])

# Set training variables
train_data_dir = '../imgs/submitted/'
batch_size = 100

images = []
category = []
for folder in os.listdir(train_data_dir):
    if os.path.isdir(f'{train_data_dir}/{folder}/') and folder != '.DS_Store':
        for name in os.listdir(f"{train_data_dir}/{folder}"):
            images.append(f"{train_data_dir}/{folder}/{name}")
            category.append(folder)

# prrocess and train test split
X_train, X_test, y_train, y_test = preprocess_images_labels(images, category)
# define new model
new_model = define_model()
# fit
new_model.fit_generator(imageLoader(X_train, y_train, 30), epochs=20, steps_per_epoch=500, verbose=0, shuffle=True)
# save model
new_version = model.get_latest_online_model_version() + 1
new_model.save(f"online-model-v{new_version}.h5")
model.publish_model(f'./online-model-v{new_version}.h5', '', 'online-model', '')
os.remove(f'./online-model-v{new_version}.h5')