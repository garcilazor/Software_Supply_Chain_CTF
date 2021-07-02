#!/bin/bash
# This script is used for easier developing of cdw containers. docker-compose will pull from 
# these builds instead of online.

docker build player --tag ctf-cdw-player
docker build randomclient --tag ctf-cdw-randomclient
docker build webserver --tag ctf-cdw-codetrov