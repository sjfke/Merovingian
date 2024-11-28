# Use an official Python runtime as the base image
# https://hub.docker.com/_/python/
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure it never exits
ENTRYPOINT ["tail", "-f", "/dev/null"]

