# Stage 1: Build the Angular frontend
FROM node:16 AS frontend-builder
WORKDIR /app
COPY ../frontend/package.json ../frontend/package-lock.json ./
RUN npm install
COPY ../frontend ./
RUN npm run build

# Stage 2: Build the Python backend
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY --from=frontend-builder /app/dist/frontend /app/static

# Command to run the application
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]