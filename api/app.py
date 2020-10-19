# from pymongo import MongoClient
# from bson.objectid import ObjectId

# local deployment
# client = MongoClient()
# db = client.Playlister # replace Playlister with database name
# playlists = db.playlists # replace playlists with collection name

import os

import numpy as np
from PIL import Image

import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from werkzeug.datastructures import FileStorage
# from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version="1.0", title="Anomaly Detection", description="")
ns = api.namespace('index')

single_parser = api.parser()
single_parser.add_argument("file", location="files", type=FileStorage, required=True)

# DON'T UPLOAD YOUR MODEL IN THE BODY OF YOUR ROUTE FUNCTION
# model will be loaded every time a request comes in
# TODO: REPLACE THIS WITH GOOGLE DRIVE LINK
# https://drive.google.com/file/d/1nBnJVWhAF7UDfKQAkDvUmF-NKpyXHShP/view?usp=sharing
model = load_model("/Volumes/Tasfia's HD/raptor/models/model.h5") 
graph = tf.get_default_graph()

label_encoder = LabelEncoder()
label_encoder.classes_ = np.load("classes.npy")

@app.route("/", methods=["GET"])
def index():
    return "<h1>Home page</h1>"


@app.route("/upload", methods=["POST"])
def upload_image():
    # add image to db 
    return


@app.route("/binary", methods=["GET"])
def binary():
    return "<h1>binary classification model</h1>"


# @app.route("/multi", methods=["GET"])
@ns.route("/multi")
class MultiClassification(Resource):
    @api.doc(parser=single_parser, description='Upload an image of a solar panel')
    def post(self):
        args = single_parser.parse_args()
        image_file = args.file
        img = Image.open(image_file)
        image_resize = img.resize((40, 24))
        image = img_to_array(image_resize)
        x = image.reshape(1, 40, 24, 1)
        x = x / 255
        with graph.as_default():
            out = model.predict_classes(x)

        pred = label_encoder.inverse_transform(out)

        return {'prediction': str(pred)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))
