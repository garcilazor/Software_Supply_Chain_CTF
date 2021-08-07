FROM ubuntu:latest

VOLUME /out
COPY ./setup /data

ENTRYPOINT /bin/bash -c 'cp /data/* /out'
