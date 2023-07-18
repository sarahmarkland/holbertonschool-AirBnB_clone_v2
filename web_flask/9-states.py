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
route /states/<id>: display a HTML page: (inside the tag BODY)
H1 tag: “State”
H3 tag: “Cities:”
UL tag: with the list of City objects linked to the State sorted by name
LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template('9-states.html', states=states.values())

@app.route('/states/<id>', strict_slashes=False)
def states_list_id(id):
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
