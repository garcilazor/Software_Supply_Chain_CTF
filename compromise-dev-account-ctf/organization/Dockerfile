FROM ubuntu:latest

ENV FLASK_APP=app
ENV FLAG=COMPROMISE-DEV-ACCOUNT-FLAG

WORKDIR /home/app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install psmisc -y
RUN pip3 install --upgrade pip
RUN pip3 install flask

COPY app/app.py /home/app/ 
COPY ./run.sh /home/app/
COPY ./README.md /home/app

RUN chmod a+x /home/app/run.sh
ENTRYPOINT ["/home/app/run.sh"]
