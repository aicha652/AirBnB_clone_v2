#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_funct():
    """define state_funct function"""
    states = storage.all(State).order_by(State.name)
    render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
