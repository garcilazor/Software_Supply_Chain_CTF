#!/bin/bash

docker stop fd-ctf-client
docker stop fd-ctf-server
docker rm fd-ctf-client
docker rm fd-ctf-server
docker network rm fd-ctf-network
