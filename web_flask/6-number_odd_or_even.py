#!/usr/bin/python3
'''
start a flask web application
listening on 0.0.0.0 port 5000
route / that returns a string
route /hbnb that returns a string
route /c/<text> that returns a string with text variable
route /python/(<text>) that returns a string with text variable
route /number/<n> that displays "n is a number" only if n is an integer
route /number_template/<n> that displays a HTML page only if n is an integer
route /number_odd_or_even/<n> that displays a HTML page only if n is an integer
and displays if n is even or odd
'''
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    returns a string that starts with "n is a number" only if n is an integer
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    render an HTML page at the /number_odd_or_even/<n> route, only if n is an
    integer
    '''
    num_type = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
