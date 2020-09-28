Model Pipeline

This folder for the model development pipline to make traning and 
updating the model quick and easy through a series of commands.

Here are main steps of this process:
    1. Data Validation
    2. Data preparation
    3. Model Traning
    4. Model evaluation
    5. Model validation
    6. Model deployment (may be in another module)

1. Data Validation
    This is the step where the image are confirmed to be the right images being sent to the image preparation.

2. Data Preparation
    Here is where the images are preprocessed and transformed into features to be used in the model traning.

3. Model Training 
    Durning this step the model is trained based on the model configuation and the using hyperparameters given through a start training command. 

4. Model Evaluation
    This step will use evaluation metrics not determined yet.

5. Model Validation
    This step is where the tranined model is validated to confirm its accuracy.

6. Model Deployment 
    Here the model is deployed either straight to the api or some model registry.

The end goal of this folder/module is to have a commandline service to make traning new model easy an quick so that more iterations can be made. 