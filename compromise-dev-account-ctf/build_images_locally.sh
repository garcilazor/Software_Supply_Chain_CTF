#!/bin/bash
# This script is used for easier developing of cdw containers. docker-compose will pull from 
# these builds instead of online.

docker build gitea --tag sscsctf/levels:ctf-cda-gitea
docker build organization --tag sscsctf/levels:ctf-cda-organization
docker build player --tag sscsctf/levels:ctf-cda-player

#docker push sscsctf/levels:ctf-cda-gitea
#docker push sscsctf/levels:ctf-cda-organization
#docker push sscsctf/levels:ctf-cda-player
