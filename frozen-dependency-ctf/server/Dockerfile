# Use Ubuntu (proviously Google Cloud SDK) container as the base image
FROM ubuntu:20.04

# Specify the maintainer of the container image
MAINTAINER Caspar "cchilds@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN apt-get update -y \
        && apt-get install -y python3-pip git vim \
        && pip3 install -r requirements.txt

EXPOSE 8000

# Set the parameters to the program
#CMD exec gunicorn --bind 0.0.0.0:8000 app:app
CMD python3 app.py

