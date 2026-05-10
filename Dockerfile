FROM python:3.11-slim

WORKDIR /app

# System packages required by python deps and the healthcheck (curl)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application source
COPY . .

# Persistent data (mounted as a volume in docker-compose)
RUN mkdir -p /app/data

# Network port — overridable at runtime via the PORT env var
ENV PORT=8400 \
    HOST=0.0.0.0
EXPOSE 8400

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -fsS "http://localhost:${PORT}/" || exit 1

CMD ["python", "main.py"]
