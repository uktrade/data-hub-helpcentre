FROM python:3.9.4

ENV POETRY_VIRTUALENVS_CREATE=false

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip pip-tools
RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry install --with dev --without production
