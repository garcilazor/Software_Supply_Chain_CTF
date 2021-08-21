#!/bin/bash

docker stop ctf-fd-client
docker stop ctf-fd-server
docker rm ctf-fd-client
docker rm ctf-fd-server
docker network rm ctf-fd-network
