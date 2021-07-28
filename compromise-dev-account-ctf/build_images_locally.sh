#!/bin/bash
# This script is used for easier developing of cdw containers. docker-compose will pull from 
# these builds instead of online.

docker build db --tag ctf-cda-db
docker build gitea --tag ctf-cda-gitea
docker build organization --tag ctf-cda-organization