FROM python:3.11

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install https://download.pytorch.org/whl/cpu-cxx11-abi/torch-2.0.0%2Bcpu.cxx11.abi-cp310-cp310-linux_x86_64.whl#sha256=c334eeb746b1ca896ba6be84d3a9796b1f9b74efa1a5a818662c9b9d59f97550
                
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /code

ENTRYPOINT ["python", "app.py"]