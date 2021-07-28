FROM ubuntu:latest

WORKDIR /home/user

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install vim -y


COPY ./malicious_script.py /home/user/

RUN chmod a+x /home/user/malicious_script.py
