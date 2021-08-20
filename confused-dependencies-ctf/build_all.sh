#!/bin/sh
set -e

docker build . -f public.Dockerfile -t sscsctf/levels:ctf-cd-public
docker build . -f private.Dockerfile -t sscsctf/levels:ctf-cd-private
docker build . -f client.Dockerfile -t sscsctf/levels:ctf-cd-client
docker build . -f tester.Dockerfile -t sscsctf/levels:ctf-cd-tester
docker build . -f setup.Dockerfile -t sscsctf/levels:ctf-cd-setup

# These will need to be pushed before the CTF is good to go live
#docker push sscsctf/levels:ctf-cd-public
#docker push sscsctf/levels:ctf-cd-private
#docker push sscsctf/levels:ctf-cd-client
#docker push sscsctf/levels:ctf-cd-tester
#docker push sscsctf/levels:ctf-cd-setup

