FROM ubuntu:latest

VOLUME /out
COPY ./public /data

ENTRYPOINT /bin/bash -c 'cp /data/* /out'
