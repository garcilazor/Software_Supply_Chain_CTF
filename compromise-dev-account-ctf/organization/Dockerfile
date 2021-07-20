FROM ubuntu:latest

ENV FLASK_APP=app

WORKDIR /home/app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y
RUN pip3 install --upgrade pip
RUN pip3 install flask

COPY app/app.py /home/app/ 
COPY ./run.sh /home/app/

RUN chmod a+x /home/app/run.sh

CMD /home/app/run.sh
