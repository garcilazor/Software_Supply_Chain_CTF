#!/bin/python3

from flask import Flask
from mysoftlog import LogConnection
import pendulum

app = Flask(__name__)

@app.route('/')
def index():
    now = pendulum.now("UTC")

    log.info("Time Server accessed at {}".format(now.isoformat()))

    pdx = now.in_tz("America/Los_Angeles")
    return "The time in PDX is {}".format(pdx.to_time_string())

if __name__ == "__main__":
    log = LogConnection("https://log.mysoft.example.com").with_context("userwidget_serv")
    app.run()

