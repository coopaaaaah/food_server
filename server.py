import flask
from flask import Flask
from flask_cors import CORS
import mongo_liaison

app = Flask(__name__)
CORS(app)
liaison = mongo_liaison


@app.route("/")
def root():
    return "You can view food at our /api/v1/food/<food_id> endpoint! Give it a try with 01001."


@app.route("/api/v1/food/<food_id>")
def get_food_by_id(food_id):
    return flask.Response(response=liaison.get_document_by_id(food_id), status=200, mimetype='application/json')


@app.route("/api/v1/food")
def get_food():
    return flask.Response(response=liaison.get_food_ids(), status=200, mimetype='application/json')


# what is this doing ?
if __name__ == "__main__":
    app.run()
