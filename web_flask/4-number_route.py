#!/usr/bin/python3
'''
start a flask web application
listening on 0.0.0.0 port 5000
route / that returns a string
route /hbnb that returns a string
route /c/<text> that returns a string with text variable
route /python/(<text>) that returns a string with text variable
route /number/<n> that displays "n is a number" only if n is an integer
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    When a user visits a URL that matches this pattern, Flask captures
    the value of <text> and passes it as an argument to the c_text function.
    returns a string that starts with "C " (the letter C followed by a space),
    and then it appends the modified text value.
    '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    '''
    returns a string that starts with "Python " appends the modified text
    value.
    '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    returns a string that starts with "n is a number" only if n is an integer
    '''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
