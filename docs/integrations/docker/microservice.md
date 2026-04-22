# Docker Deployment: Probo as Microservice Backend-for-Frontend (BFF)

This guide shows how to containerize a **Probo UI** application as a production-ready microservice that serves as a **Backend-for-Frontend (BFF)**.

In this architecture, Probo acts as the dedicated UI layer: it receives requests from the frontend (or mobile), fetches data from backend services (Django API, FastAPI, databases, etc.), renders beautiful HTML/components using Probo, and streams the response back.

---

## Why Run Probo as a BFF Microservice?

- Separation of concerns: Backend APIs stay clean, UI logic lives in Probo
- Independent scaling of UI layer
- Easier frontend development (just call Probo endpoints)
- Excellent HTMX + streaming support
- Can serve multiple frontends (web, mobile web, etc.)?

---

## 1. Recommended Dockerfile (Production Ready)

Create `Dockerfile` in your project root:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv for fast dependency management (optional but recommended)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock* requirements.txt* ./

# Install dependencies
RUN uv pip install --system --no-cache-dir -e . \
    && uv pip install --system --no-cache-dir gunicorn uvicorn[standard]

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run with Gunicorn + Uvicorn workers (best for production)
CMD ["gunicorn", "app.main:app", \
     "-k", "uvicorn.workers.UvicornWorker", \
     "-w", "4", \
     "--bind", "0.0.0.0:8000", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]
```
- **Note:** Replace app.main:app with your actual app entry point (e.g. probo_app:app or main:app).

# 2. docker-compose.yml Example (BFF Setup)
```YAML 
version: '3.9'

services:
  probo-bff:
    build: .
    container_name: probo-bff
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - ENVIRONMENT=production
      # Add your backend API URLs here
      - BACKEND_API_URL=http://backend:8001
    depends_on:
      - backend
    restart: unless-stopped

  # Example: Your main backend service
  backend:
    image: your-backend-image:latest
    container_name: probo-backend
    ports:
      - "8001:8000"
    environment:
      - DATABASE_URL=...
    restart: unless-stopped

  # Optional: Reverse proxy (Nginx or Caddy)
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - probo-bff
```
# 3. Basic Nginx Config (Reverse Proxy)
```nginx
# nginx.conf
upstream probo_bff {
    server probo-bff:8000;
}

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://probo_bff;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
# 4. Probo CLI + Docker Workflow
### Since Probo has built-in CLI support:
```Bash
# Build and run locally
docker compose up --build

# Or use Probo CLI if you have it configured
probo run main:app # gunicord
#probo run main::app # uvicorn
```
# Best Practices for Probo BFF

- Use Gunicorn + Uvicorn workers for production (not plain uvicorn)
- Enable streaming (.stream()) for large pages and reports
- Set proper worker count: (2 × CPU cores) + 1
- Use multi-stage builds to keep image size small
- Add healthcheck endpoint (/health)
- Separate static files (CSS/JS) and serve them via Nginx or Caddy
- Use environment variables for configuration
