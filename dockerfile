# ===== FRONTEND BUILD =====
FROM node:23.6.0 AS frontend-builder

WORKDIR /app
COPY frontend/package*.json ./  
RUN npm install
COPY frontend .                
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
COPY --from=backend-builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Copy backend source
COPY backend/ .         

# Copy protected files
COPY backend/protected ./protected

ENV PYTHONPATH=/app
ENV APP_ENV=production

# Runtime configuration
ENV FLASK_APP=app.py            
ENV FLASK_ENV=production
EXPOSE 8081
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--workers", "1"]