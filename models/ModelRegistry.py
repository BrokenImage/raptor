import json
import enum


class ModelRegistry:
    def __init__(self, db, collection_name='models'):
        self.conn = db.collection_name

    class stages(enum.Enum):
        development = "DEVELOPMENT"
        production = "PRODUCTION"

    def publish_model(self, model, name, metrics):
        version = 1
        remote_path = 's3://models/{}::v{}'.format(name, version)
        # TODO: Upload model to aws s3 bucket
        model_doc = {name, version, remote_path,  metrics, "stage": self.stages.development}
        self._insert((name, version, metrics_str, remote_path))

    def increment_version(self, model, name, metrics):
        # Get the most recent model version doc in the collection
        initial_model = self.conn.find(
            {"name": name}).sort({"version": -1}).limit(1)

        # Increment the version by one
        version = initial_model.version
        new_version = version + 1

        # Upload the model to aws s3
        remote_path = 's3://models/{}::v{}'.format(name, new_version)
        # TODO: Upload model to aws s3 bucket

        # Upload model doc to database
        model_doc = {name, version, remote_path,  metrics}
        self.conn.insert_one(model_doc)

    def update_stage(self, name, version, stage):
        query = {"name": name, "version", version}
        new_values = {"$set": {"stage": stage}}
        self.conn.update_one({"name"})

    def get_production_model(self, name):
        return self.conn.find_one({"name": name, "stage": self.stages.production})
