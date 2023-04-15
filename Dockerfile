FROM alpine:latest

COPY . .

RUN apk add --no-cache --update python3 py3-pip bash

RUN pip install Flask

RUN pip install requests

RUN pip install gunicorn

RUN adduser -D userA

USER userA

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
