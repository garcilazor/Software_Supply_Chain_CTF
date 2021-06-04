FROM ubuntu:latest

COPY ./requirements.txt /testLevel/requirements.txt

WORKDIR /testLevel

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./* /testLevel/

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
