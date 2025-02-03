# ===== FRONTEND BUILD =====
FROM node:23.6.0 AS frontend-builder

WORKDIR /app
COPY frontend/package*.json ./  
RUN npm install
COPY frontend/ .                
RUN npm run build

# ===== BACKEND BUILD =====
FROM python:3.11-slim AS backend

WORKDIR /app
COPY backend/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# ===== PRODUCTION IMAGE =====
FROM python:3.11-slim
WORKDIR /app

# Copy Python dependencies
COPY --from=backend /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy backend source
COPY backend/ .                

# Copy frontend build artifacts
COPY --from=frontend-builder /app/dist ./frontend-dist

# Runtime configuration
ENV FLASK_APP=app.py            
ENV FLASK_ENV=production
EXPOSE 8081
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8081", "--workers", "4"] 