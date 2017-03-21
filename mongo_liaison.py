from bson.json_util import dumps
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['usda']
collection = db['nutrition']


def get_document_by_id(post_id):
    document = collection.find_one({"_id": post_id})

    if document is None:
        return 'No object found'
    else:
        return dumps(document, sort_keys = True, indent = 4, separators = (',', ': '))


def get_food_ids():

    food_ids = []

    for doc in collection.find({}):
        food_ids.append(doc['_id'])

    return dumps(food_ids, sort_keys = True, indent = 4, separators = (',', ': '))

