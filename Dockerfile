# Stage 1: Build dependencies
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /

RUN apt-get update && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*
    
# Stage 2: Final image (minimal)
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PATH="/root/.local/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org \
--trusted-host files.pythonhosted.org -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
