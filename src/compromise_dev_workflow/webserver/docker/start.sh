#!/bin/bash

service ssh start
sudo -u appuser gunicorn --bind 0.0.0.0:8080 webserver:app