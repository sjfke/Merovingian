# Use an official alpine runtime as the base image
# https://hub.docker.com/_/python/
FROM alpine:latest

# Install python/pip and have 'UNBUFFERED' python output 
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python && mkdir /home/src && cd /home/src
RUN python -m venv venv
# RUN /home/src/bin/activate && pip install --no-cache --upgrade pip setuptools && pip install --no-cache-dir -r requirements.txt
# RUN pip3 install --no-cache --upgrade pip setuptools
# RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
