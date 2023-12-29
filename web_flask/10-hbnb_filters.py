#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters_funct():
    """Define a filters_funct function"""
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    for state in states:
        state.cities = sorted([city for city in storage.all(City).values()
                               if city.state_id == state.id], key=lambda
                              city: city.name)
    return render_template("10-hbnb_filters.html", amenities=amenities, states=states)


@app.teardown_appcontext
def teardown_funct(self):
    """Define a teardown_funct function"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
