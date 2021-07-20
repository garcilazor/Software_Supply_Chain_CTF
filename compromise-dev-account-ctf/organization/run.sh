#!/bin/bash

while true
do
	kill -9 $(pgrep -f flask)
	pip install git+http://gitea/pallets/flask.git
	flask run
	sleep 30
done
