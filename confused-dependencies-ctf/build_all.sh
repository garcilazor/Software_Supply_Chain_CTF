#!/bin/sh

docker build . -f public.Dockerfile -t sscsctf/levels:confused-dependencies-public
docker build . -f private.Dockerfile -t sscsctf/levels:confused-dependencies-private
docker build . -f client.Dockerfile -t sscsctf/levels:confused-dependencies-client
docker build . -f tester.Dockerfile -t sscsctf/levels:confused-dependencies-tester
docker build . -f setup.Dockerfile -t sscsctf/levels:confused-dependencies-setup

docker push sscsctf/levels:confused-dependencies-public
docker push sscsctf/levels:confused-dependencies-private
docker push sscsctf/levels:confused-dependencies-client
docker push sscsctf/levels:confused-dependencies-tester
docker push sscsctf/levels:confused-dependencies-setup

