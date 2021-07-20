#!/bin/bash

while true
do
	pip install > "git+http://gitea/pallets.flask"
	flask run
	sleep 30
	kill $(pgrep -f flask)
done
