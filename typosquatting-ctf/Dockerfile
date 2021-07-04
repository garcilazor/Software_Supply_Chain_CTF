FROM ubuntu:latest

WORKDIR /app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install vim -y\
    && apt-get install python3 -y\
    && apt-get install python3.8-venv -y
RUN pip3 install --upgrade pip
RUN git clone https://github.com/catrionamckay/typosquatting-env.git
RUN pip install /app/typosquatting-env/pytxdata
RUN pip install /app/typosquatting-env/pendulum
RUN pip install /app/typosquatting-env/flask


