#!/usr/bin/python3
"""
script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def textC(text):
    new_text = text.replace("_", " ")
    return ('C ' + new_text)

@app.route('/python/<text>', strict_slashes=False)
def textPython(text='is cool'):
    new_text = text.replace("_", " ")
    return ('Python' + new_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
