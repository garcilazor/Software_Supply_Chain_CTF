from flask import Flask, abort
import pendulum
import urllib3
import PyQt5
import pytest
import requests
import pandas
import matplotlib
import arrow
import scipy
import sqlalchemy
import cirq

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "You know what they say more dependencies more problems"

@app.route("/error")
def error():
    abort(500, "Whoops something went wrong")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
