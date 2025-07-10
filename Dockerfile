# ---------- Stage 1: Base image with setup tools ----------
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install required system tools
RUN apt-get update && apt-get install -y  gcc libpq-dev

WORKDIR /app

# Copy only requirements for dependency install
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org \
--trusted-host files.pythonhosted.org -r requirements.txt

# ---------- Stage 2: Final lightweight app image ----------
FROM python:3.13-slim AS final
RUN apt-get update && apt-get install -y postgresql-client
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /usr/local /usr/local

# ✅ Copy the wait script and app code
COPY wait_for_db.sh .
COPY . .

# Make sure wait script is executable
RUN chmod +x wait_for_db.sh

EXPOSE 8000

CMD ["sh", "-c", "./wait_for_db.sh && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
