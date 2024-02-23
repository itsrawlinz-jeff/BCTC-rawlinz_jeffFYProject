FROM python:3.11

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-win_amd64.whl#sha256=e060c3a19789e71314d0e2a5d40da9eb2743d59170b0aab6c3ce5cf3b7801a44
                
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /code

ENTRYPOINT ["python", "app.py"]