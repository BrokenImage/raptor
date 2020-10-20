from pymongo import MongoClient

image_schema = {
    "path": {
        "type": "string",
        "required": True
    },
    "name": {
        "type": "string",
        "required": True
    },
    "anomaly": {
        "type": "string"
    },
    "origin": {
        "type": "string" # replace with list, ["user", "self"]
    },
    "date": {
        "type:" "string" # replace with datetime obj
    }
}