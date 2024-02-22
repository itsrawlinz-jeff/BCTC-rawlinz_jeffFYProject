FROM python:3.10-slim

ADD . /code
WORKDIR /code

ENTRYPOINT [ "python", "app.py" ]