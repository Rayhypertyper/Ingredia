# Lightweight Dockerfile for hosting the FastAPI app on Hugging Face (or other container hosts).
# Notes:
# - Mount Google credentials (if using Cloud Vision) into the container and set GOOGLE_APPLICATION_CREDENTIALS.
# - Hugging Face sets $PORT for the container; fallback to 8080 when not provided.

FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

# System packages required by OpenCV, ffmpeg and many ML libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    git \
    curl \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency file first to leverage Docker layer caching
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install dependencies (prefer binary wheels)
RUN pip install --upgrade pip setuptools wheel \
 && pip install --upgrade --prefer-binary -r /app/requirements.txt

# Copy application code
COPY . /app

# Create non-root user and adjust ownership
RUN useradd -m appuser || true \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

# If you use Google Vision, mount the service account JSON at /app/gcloud.json and set:
#   -e GOOGLE_APPLICATION_CREDENTIALS=/app/gcloud.json
# Example Hugging Face Secrets / Docker run:  -v /local/key.json:/app/gcloud.json -e GOOGLE_APPLICATION_CREDENTIALS=/app/gcloud.json
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080} --workers