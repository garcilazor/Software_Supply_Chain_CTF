FROM ubuntu:latest

RUN useradd --create-home somedeveloper
WORKDIR /home/somedeveloper
USER somedeveloper
COPY ./flag .

# curl-bash the webserver every 30 seconds
# CMD ["watch", "-n30", "bash", "(curl http://{webservername}/upload)"]