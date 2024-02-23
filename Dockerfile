FROM python:3.11

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install https://download.pytorch.org/whl/cpu/torch-1.4.0%2Bcpu-cp38-cp38-win_amd64.whl
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /code

ENTRYPOINT ["python", "app.py"]