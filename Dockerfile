FROM python:3.10-slim


COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code
WORKDIR /code

ENTRYPOINT [ "python", "app.py" ]