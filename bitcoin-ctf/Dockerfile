# Use Google Cloud SDK's container as the base image
FROM ubuntu:latest

# Specify the maintainer of the container image
MAINTAINER Caspar "cchilds@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN apt-get update -y 
RUN apt-get install -y python3-pip && apt-get install -y git && pip3 install -r requirements.txt

# Set the parameters to the program
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
CMD python3 app.py

