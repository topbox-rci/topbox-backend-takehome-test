from bson import json_util, ObjectId
from flask import Flask

from app.helpers import mongo_client

API_VERSION = '1.0'

app = Flask(__name__)
db = mongo_client()


@app.route('/')
def root():
    response = {'apiVersion': API_VERSION, 'appName': 'Topbox Backend Take Home Test'}
    return json_util.dumps(response)


@app.route('/clients')
def clients():
    return json_util.dumps(db.clients.find({}))


@app.route('/clients/<client_id>')
def clients_by_id(client_id):
    client_object_id = ObjectId(client_id)
    return json_util.dumps(db.clients.find_one({'_id': client_object_id}))


@app.route('/engagements')
def engagements():
    return json_util.dumps(db.engagements.find({}))


@app.route('/engagements/<engagement_id>')
def engagements_by_id(engagement_id):
    engagement_object_id = ObjectId(engagement_id)
    return json_util.dumps(db.engagements.find_one({'_id': engagement_object_id}))


@app.route('/interactions')
def interactions():
    return json_util.dumps(db.interactions.find({}))
