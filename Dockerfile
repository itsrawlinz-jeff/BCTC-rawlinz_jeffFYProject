FROM python:3.10-slim AS build

WORKDIR /code
COPY requirements.txt .
RUN pip wheel -r requirements.txt -w /wheels

FROM python:3.10-slim  
WORKDIR /code
COPY --from=build /wheels /wheels
RUN pip install --no-index /wheels/*

COPY . .
ENTRYPOINT ["python", "app.py"]