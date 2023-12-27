#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_funct():
    """Define a cities_funct function"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    for state in states:
        state.cities = sorted([city for city in storage.all(City).values()
                               if city.state_id == state.id], key=lambda
                              city: city.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_funct(self):
    """Define a teardown_funct function"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
