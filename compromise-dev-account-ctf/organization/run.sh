#!/bin/bash
sleep 20
while true
do
	pip install git+http://gitea/pallets/flask.git
	flask run --host=$(hostname -I) -p 80 &
	sleep 10
	fuser -k 80/tcp
done
