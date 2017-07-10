# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Watson Discovery service based search of LCNF, NIA and NIC docs
#Provides listing of top earch results and detail for each document

import os
from flask import Flask, jsonify
import flask
#Use CORS to make API available to any client
#https://pypi.python.org/pypi/Flask-Cors/3.0.3
#from flask_cors import CORS, cross_origin

import math
import csv
import json
import swiftclient
import sys
import os
from watson_developer_cloud import DiscoveryV1

import credentials

DISCOVERY_USERNAME = credentials.discovery['DISCOVERY_USERNAME']
DISCOVERY_PASSWORD = credentials.discovery['DISCOVERY_PASSWORD']
ENVIRONMENT_ID = credentials.discovery['ENVIRONMENT_ID']
COLLECTION_ID = credentials.discovery['COLLECTION_ID']

discovery = DiscoveryV1(
  username = DISCOVERY_USERNAME,
  password = DISCOVERY_PASSWORD,
  version = "2017-06-25"
)

app = Flask(__name__)

#Use CORS to make this service public
#CORS(app)

#Use this to display the HTML / Javascript front end
@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return flask.send_from_directory('public',
                               filename, as_attachment=True)

#Works web servie starts here
@app.route('/api/discovery/<search>', methods=['Get'])
def search(search):

    #Strip latitude and longitude from url
    searchStr = search.split(',')[0]
    filterStr = search.split(',')[1]

    print('Searching for ' + searchStr + ', ' + filterStr )

    qopts = {'query': searchStr, 'filter': filterStr}
    qr = discovery.query(ENVIRONMENT_ID, COLLECTION_ID, qopts)

    #Convert Dictionary to json object. This could be done in return statement
    #This allows it to be printed to the console before it is returned
    retval = jsonify(qr)
    print(retval)
    return retval

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
