#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Define a hello function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define a hbnb function"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Define a funct function"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Define a python_text function"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
