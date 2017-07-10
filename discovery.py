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

#This is a simple web service that finds and returns the nearest street Works
#that are contained in a '|' delimeted file works.txt
#There is also a web service for downloading works.txt from an Object Store
#/ape/download

import os
from flask import Flask, jsonify
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

DISCOVERY_USERNAME="ddde726c-7f0c-488b-861c-dd845aa1c3f1"
DISCOVERY_PASSWORD="16DtSO03WCoD"

ENVIRONMENT_ID="7c98c384-8455-4aab-b54f-bb91065ca390"
COLLECTION_ID="74f48674-41b2-47c3-b041-df802dd451dd"

discovery = DiscoveryV1(
  username=DISCOVERY_USERNAME,
  password=DISCOVERY_PASSWORD,
  version="2017-06-25"
)

app = Flask(__name__)

#Use CORS to make this service public
#CORS(app)

#Use this to display the HTML / Javascript front end
@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


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
