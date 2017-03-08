from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['usda']
collection = db['nutrition']


# The web framework gets post_id from the URL and passes it as a string
def get_document_by_id(post_id):
    # Convert from string to ObjectId:
    document = collection.find_one({"_id": post_id})

    if document is None:
        return 'No object found'
    else:
        return dumps(document)


def get_food_ids():

    food_ids = []

    for doc in collection.find({}):
        food_ids.append(doc['_id'])

    return dumps(food_ids)
