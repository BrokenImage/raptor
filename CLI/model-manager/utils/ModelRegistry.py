import json
import enum


class ModelRegistry:
    def __init__(self, db, s3, collection_name='models', bucket_name="models"):
        self.conn = db[collection_name]
        self.s3_bucket = s3.Bucket(bucket_name)

    class stages(enum.Enum):
        development = "DEVELOPMENT"
        production = "PRODUCTION"

    def _insert(self, name, version, metrics_str, naming_format, stage):
        model_doc = {
            "name": name, 
            "version": version, 
            "naming_format": naming_format,
            "metrics": metrics_str, 
            "stage": stage
        }
        self.conn.insert_one(model_doc)

    def publish_model(self, model_path, classes_path, name, metrics):
        # Save model file to AWS S3 bucket 
        version = 1
        self.s3_bucket.upload_file(Filename=model_path, Key=f'{name}-v{version}.h5')
        self.s3_bucket.upload_file(Filename=classes_path, Key=f'{name}-v{version}.npy')

        # Create and save a new model doc with related information
        self._insert(name, version, metrics, 'name-v0.h5', self.stages.development.value)

    def increment_version(self, model_path, classes_path, name, metrics):
        # Get the most recent model version doc in the collection
        initial_model = list(self.conn.find({"name": name}).sort([("version", -1)]).limit(1))[0]

        # Increment the version by one
        version = initial_model['version']
        new_version = version + 1

        # Upload the model to aws s3
        self.s3_bucket.upload_file(Filename=model_path, Key=f'{name}-v{new_version}.h5')
        self.s3_bucket.upload_file(Filename=classes_path, Key=f'{name}-v{new_version}.npy')

        # Upload model doc to database
        self._insert(name, new_version, metrics, 'name-v0.h5', self.stages.development.value)

    def update_stage(self, name, version, stage):
        query = {"name": name, "version": version}
        new_values = {"$set": {"stage": stage}}
        self.conn.update_one(query, new_values)

    def get_production_model(self, name):
        return self.conn.find_one({"name": name, "stage": self.stages.production})
