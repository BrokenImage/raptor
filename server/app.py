from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from bson.objectid import ObjectId
import os
from datetime import datetime

# local deployment
# client = MongoClient()
# db = client.Playlister # replace Playlister with database name
# playlists = db.playlists # replace playlists with collection name

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Home page</h1>"


@app.route("/binary", methods=["GET"])
def binary():
    return "<h1>binary classification model</h1>"


@app.route("/multi", methods=["GET"])
def multi():
    return "<h1>multi-classification model</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))
