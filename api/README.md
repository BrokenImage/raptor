Prediction API

This folder is for the prediction api that will take in an image 
as input and output a anomalies classification for the given image.

There are two main parts of this API:

1. Model Registry  
    The model registry is a database of models that contain old and new models that have been or are going to be used in the preidction api

2. Prediction API  
    The prediction api will pull the latest and deployable model from the model registry to make prediction for the website and possible clients.

The end goal of this module is to have an secure api for making prediction with the models developed from the model development module/folder. (The website may be ran from this service as well for a more secure connection to it)