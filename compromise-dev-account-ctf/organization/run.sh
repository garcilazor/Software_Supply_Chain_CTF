#!/bin/bash

while true
do
	kill -9 $(pgrep -f flask)
	pip install git+http://gitea/pallets/flask.git
	flask run --host=$(hostname -I) -p 80
	sleep 30
done
