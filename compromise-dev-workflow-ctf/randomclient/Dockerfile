FROM ubuntu:kinetic-20220830

RUN apt-get update && apt-get install -y curl

ENV TROVTOKEN b54337b2-35ee-4bad-a74e-83f05394f393
ENV TROVUPLOADDIRECTORY /home/somedeveloper/junit

COPY start.sh /var/
RUN chmod u+x /var/start.sh

RUN useradd --create-home somedeveloper
RUN mkdir -p /home/somedeveloper/junit
RUN mkdir -p /home/somedeveloper/.ssh
WORKDIR /home/somedeveloper
USER somedeveloper
COPY testResults.xml /home/somedeveloper/junit
COPY .bashrc /home/somedeveloper
COPY ssh/flag /home/somedeveloper/.ssh/flag
COPY ssh/ssh /home/somedeveloper/.ssh/.ssh
COPY ssh/ssh.pub /home/somedeveloper/.ssh/.ssh.pub

CMD ["/var/start.sh"]
