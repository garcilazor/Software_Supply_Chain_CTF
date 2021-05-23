FROM ubuntu:latest

ENV TROVTOKEN b54337b2-35ee-4bad-a74e-83f05394f393
ENV TROVUPLOADDIRECTORY /home/somedeveloper/junit

RUN useradd --create-home somedeveloper
WORKDIR /home/somedeveloper
USER somedeveloper
COPY ./flag .


# curl-bash the webserver every 30 seconds
# CMD ["watch", "-n30", "bash", "(curl http://{webservername}/upload)"]