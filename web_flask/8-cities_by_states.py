#!/usr/bin/python3
"""
Script that starts a Flask web app
Listens on 0.0.0.0, port 5000
Uses storage for fetching data from the storage engine (FileStorage or
DBStorage)
Remove the current SQLAlchemy Session after each request
Routes: /states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name
LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    cities = storage.all("City")
    return render_template('8-states_list.html', states=states.values(),
                           cities=cities.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
