#!/bin/bash
# This script is used for easier developing of cdw containers. docker-compose will pull from 
# these builds instead of online.

docker build player --tag sscsctf/levels:ctf-cdw-player
docker build randomclient --tag sscsctf/levels:ctf-cdw-randomclient
docker build webserver --tag sscsctf/levels:ctf-cdw-codetrov

#docker push sscsctf/levels:ctf-cdw-player
#docker push sscsctf/levels:ctf-cdw-codetrov
#docker push sscsctf/levels:ctf-cdw-randomclient
