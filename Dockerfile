# Multi-stage build: Frontend
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build

# Backend stage
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    openjdk-17-jdk \
    maven \
    && rm -rf /var/lib/apt/lists/*

# Copy backend files
COPY java-migration-backend/Java_Migration_Accelerator_backend/java-migration-backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY java-migration-backend/Java_Migration_Accelerator_backend/java-migration-backend/ .

# Copy built frontend from builder stage
COPY --from=frontend-builder /app/frontend/dist /app/static

# Create necessary directories
RUN mkdir -p /tmp/migrations /app/logs

# Expose ports (backend on 8001, frontend served via backend)
EXPOSE 8001

# Set environment variables
ENV PYTHONPATH=/app:$PYTHONPATH
ENV WORK_DIR=/tmp/migrations

# Start the backend server (it will serve static frontend files)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]