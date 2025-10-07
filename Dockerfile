# Simple production-ready container for Cloud Run
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run expects the service to listen on $PORT (default 8080)
ENV PORT=8080

# Use gunicorn in container
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
