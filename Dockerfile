# Dockerfile
FROM python:3.11-slim
WORKDIR /app

# Install deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run will provide $PORT
ENV PORT=8080

# Use gunicorn to serve Flask app object "app" in main.py
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
