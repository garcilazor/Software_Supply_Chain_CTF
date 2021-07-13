#!/bin/python3


from flask import Flask
import pendulum

app = Flask(__name__)

@app.route('/')
def hello():
    now = pendulum.now("UTC")

    print("server accessed at {}".format(now.isoformat()))

    pdx = now.in_tz("America/Los_Angeles")
    return "The time in PDX is {}".format(pdx.to_time_string())

app.run()
