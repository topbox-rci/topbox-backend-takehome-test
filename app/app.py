from bson import json_util
from flask import Flask

from app import __version__
from app.helpers import mongo_client

API_VERSION = __version__

app = Flask(__name__)
db = mongo_client()


@app.route('/')
def root():
    response = {'apiVersion': API_VERSION, 'appName': 'Topbox Backend Take Home Test'}
    return json_util.dumps(response)


@app.route('/clients')
def clients():
    return json_util.dumps(db.clients.find({}))


@app.route('/engagements')
def engagements():
    return json_util.dumps(db.engagements.find({}))


@app.route('/interactions')
def interactions():
    return json_util.dumps(db.interactions.find({}))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
