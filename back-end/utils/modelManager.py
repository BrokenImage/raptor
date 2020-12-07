import os
import re
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelEncoder

class ModelManager():
    def __init__(self, db, s3, graph, backup_model, backup_label_encoder, collection_name='models', bucket_name='models'):
        self.conn = db[collection_name]
        self.s3_bucket = s3.Bucket(bucket_name)
        self.label_encoder = LabelEncoder()
        self.model = None
        self.backup_model = backup_model
        self.backup_label_encoder = backup_label_encoder
        self.graph = graph

    def predict(self, image_array):
        """Function that accepts a model and image_array and returns a prediction."""
        if self.model:
            with self.graph.as_default():
                out = self.model.predict_classes(image_array)
            return self.label_encoder.inverse_transform(out)
        with self.graph.as_default():
            out = self.backup_model.predict_classes(image_array)
        return self.backup_label_encoder.inverse_transform(out)
            
    def preprocess(self, image_file):
        """Preprocess the given image file by resizing and turning it into an array."""
        img = Image.open(image_file)
        image_resize = img.resize((40, 24))
        image = img_to_array(image_resize)
        x = image.reshape(1, 40, 24, 1)
        return  x / 255

    def load(self, model_path, label_encoder_path):
        """Load a fitted model from the local filesystem into memory. "./models/classes.npy"""
        self.label_encoder.classes_ = np.load(label_encoder_path)
        self.model = load_model(model_path)

    def load_latest_model(self):
        """Load a fitted model from a remote filesystem into memory."""
        latest_model = list(self.conn.find({'stage': 'PRODUCTION'}).sort([("version", -1)]).limit(1))
        if len(latest_model) == 0:
            return

        latest_model = latest_model[0]
        if 'MODEL_NAME' in os.environ and latest_model['name'] == os.environ['MODEL_NAME']:
            if 'MODEL_VERSION' in os.environ and str(latest_model['version']) == os.environ['MODEL_VERSION']:
                return

        for f in os.listdir('./models'):
            if not f.endswith(".h5") and not f.endswith(".npy"):
                continue
            os.remove(os.path.join('./models', f))
        
        # Download model h5 file
        model = re.sub('name', latest_model['name'], latest_model['naming_format'])
        model = re.sub('0', str(latest_model['version']), model)
        self.s3_bucket.download_file(model, f'./models/{model}')

        # Download model classes npy file
        classes = re.sub('name', latest_model['name'], latest_model['naming_format'])
        classes = re.sub('0', str(latest_model['version']), classes)
        classes = re.sub('h5', 'npy', classes)
        self.s3_bucket.download_file(classes, f'./models/{classes}')
        os.environ['MODEL_NAME'] = latest_model['name']
        os.environ['MODEL_VERSION'] = str(latest_model['version'])

