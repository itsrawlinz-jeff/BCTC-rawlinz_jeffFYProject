FROM python:3.11

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

RUN pip3 install https://download.pytorch.org/whl/cpu/torch-1.7.1%2Bcpu-cp38-cp38-linux_x86_64.whl
COPY . .

WORKDIR /code

ENTRYPOINT ["python", "app.py"]