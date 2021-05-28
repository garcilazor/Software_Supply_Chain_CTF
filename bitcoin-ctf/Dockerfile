FROM alpine:3.12

COPY . /app
WORKDIR /app

RUN apk add py3-pip && apk add git && pip3 install -r requirements.txt

CMD python3 app.py
