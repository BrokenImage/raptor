from pymongo import MongoClient
from sklearn.model_selection import train_test_split

# TODO: function to get new images from db, split into train and test data,
# add append to last model's train/test lists
# NOTE: assuming image has a given anomaly (not a prediction from the last model)