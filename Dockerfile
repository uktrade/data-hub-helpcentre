FROM python:3.6.13

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt
