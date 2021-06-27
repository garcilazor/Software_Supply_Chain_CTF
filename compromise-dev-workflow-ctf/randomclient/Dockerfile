FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

ENV TROVTOKEN b54337b2-35ee-4bad-a74e-83f05394f393
ENV TROVUPLOADDIRECTORY /home/somedeveloper/junit

COPY start.sh /var/
RUN chmod u+x /var/start.sh

RUN useradd --create-home somedeveloper
RUN mkdir -p /home/somedeveloper/junit
WORKDIR /home/somedeveloper
USER somedeveloper
COPY ./flag .
COPY testResults.xml /home/somedeveloper/junit

CMD ["/var/start.sh"]
