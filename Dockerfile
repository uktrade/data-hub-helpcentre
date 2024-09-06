FROM python:3.10

ENV POETRY_VIRTUALENVS_CREATE=false

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip pip-tools

RUN pip install -r requirements.txt 
