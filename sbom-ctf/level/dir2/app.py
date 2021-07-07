from flask import Flask, abort
import numpy
import flask_caching
import pendulum

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "More packages nothing to see here"

@app.route("/error")
def error():
    abort(500, "Whoops something went wrong")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
