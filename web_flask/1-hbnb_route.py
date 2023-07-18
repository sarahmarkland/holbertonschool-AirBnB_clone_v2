#!/usr/bin/python3
'''
start a flask web application
port 5000
add a route /hbnb that returns a string
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' return a string at the root route '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' return a string at the /hbnb route '''
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
