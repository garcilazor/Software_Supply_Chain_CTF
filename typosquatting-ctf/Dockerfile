FROM ubuntu:kinetic

WORKDIR /app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install vim -y\
    && apt-get install python3 -y\
    && apt-get install python3.8-venv -y\
    && DEBIAN_FRONTEND=noninteractive apt-get install tzdata -y
RUN pip3 install --upgrade pip
RUN pip install flask
RUN pip install git+https://github.com/typoctf/pytxdata.git
RUN pip install git+https://github.com/typoctf/pendulum.git

COPY server /app

ENTRYPOINT /bin/bash
