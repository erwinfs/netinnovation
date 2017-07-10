# Python Flask Network Innovations

This application demonstrates a simple, reusable Python web application based on the [Flask microframework](http://flask.pocoo.org/).
It allows users to search a Watson Discovery set that has been loaded with LCNF, NIA and NIC reports and submissions
To use this you will need credentials for a Watson Discovery service. These need to be entered into the credentials.py file.
It also allows the user to download the original reports. These are in pdf format in /public

## Run the app locally

1. [Install Python][]
1. cd into this project's root directory
1. Run `pip install -r requirements.txt` to install the app's dependencies
1. Run `python discovery.py'
1. Access the running app in a browser at <http://localhost:5000>

[Install Python]: https://www.python.org/downloads/
