FROM python:3.6
LABEL maintainer="Tracy_Martin@eogresources.com"

RUN mkdir -p /usr/src/app
RUN adduser --disabled-password --gecos '' guser
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app

EXPOSE 8000