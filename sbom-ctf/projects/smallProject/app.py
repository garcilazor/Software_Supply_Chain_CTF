from flask import Flask, abort
import meld3
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/error")
def error():
    abort(500, "Whoops something went wrong")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
