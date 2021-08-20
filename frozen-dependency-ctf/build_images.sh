#!/bin/bash

docker build client --tag sscsctf/levels:ctf-fd-client
docker build server --tag sscsctf/levels:ctf-fd-server

#docker push sscsctf/levels:ctf-fd-client
#docker push sscsctf/levels:ctf-fd-server
