from pymongo import MongoClient

model_schema = {
    "name": {
        "type": "string"
    },
    "version": {
        "type": "int",
        "required": True
    },
    "metrics": {
        "type": "string", # replace with json object
        "required": True
    },
    "aws-path": {
        "type": "string",
        "required": True
    },
    "created": {
        "type": "string" # replace with datetime object
        "required": True
    },
    "train-data": {
        "type": "string" # replace with list, [img1_id, img2_id, img3_id, ...]
    },
    "test-data": {
        "type": "string" # replace with list, [img1_id, img2_id, img3_id, ...]
    },
    "stage": {
        "type": "string"
    }
}
