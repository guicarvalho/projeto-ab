FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apk --update --upgrade add --no-cache --virtual .build-dep \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    && pip install poetry && poetry install --no-dev

CMD poetry run flask run -h 0.0.0.0 -p 5000

