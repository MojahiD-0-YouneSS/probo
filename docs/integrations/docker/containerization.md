# Deploying Probo UI with Docker

This guide shows you how to containerize and run your Probo UI application using Docker for both development and production.

Probo UI is stateless and easy to deploy because it is written in pure Python.

---

## 1. Dockerfile (Recommended)

Create a file named `Dockerfile` in the root of your project:

```dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```
# 2. requirements.txt
- Make sure your requirements.txt includes at least:
```txt
probo-ui>=1.4.0
uvicorn[standard]>=0.30.0
gunicorn>=22.0.0
```
# 3. docker-compose.yml (Recommended for local development)
Create docker-compose.yml:

```yaml
version: '3.9'

services:
  probo:
    build: .
    container_name: probo-ui
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=False
      - ENVIRONMENT=production
    restart: unless-stopped
```
# 4. How to Build and Run
### Build and run with Docker Compose:
```Bash
# Build and start the container
docker compose up --build

# Run in background (detached mode)
docker compose up -d --build
```
- Your Probo UI app will be available at: → http://localhost:8000

# Best Practices

- Workers: Set --workers to roughly 2 × CPU cores + 1 in production.
- Static Files: For better performance, put Nginx or Caddy in front of Probo to serve static files (CSS, JS, images).
- Health Check: Consider adding a simple /health endpoint in your app.
- Production CMD: In production, it's better to use Gunicorn + Uvicorn workers instead of plain Uvicorn
```yaml
CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--bind", "0.0.0.0:8000"]
```

# Quick Tips

- Use python:3.12-slim to keep your Docker image small.
- Always use --no-cache-dir when installing packages to reduce image size.
- For live reloading during development, keep the volume mount (- .:/app) and use --reload.
