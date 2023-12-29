#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_funct():
    """Define a states_funct function"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_cities(id):
    """define a states_cities function"""
    all_state = storage.all(State).values()
    for state in all_state:
        if (state.id == id):
            state.cities = sorted([city for city in storage.all(City).values()
                                   if city.state_id == state.id],
                                  key=lambda city: city.name)
            all_state = state
            break
        else:
            all_state = None
    return render_template("9-states.html", id=id, all_state=all_state)


@app.teardown_appcontext
def teardown_funct(self):
    """Define a teardown_funct function"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
