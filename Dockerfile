# Build stage
FROM python:3.11 AS build
ENV TORCH_CUDA_IS_AVAILABLE=0
WORKDIR /build
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

# Runtime stage 
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /build/app /app
CMD ["python", "app.py"]