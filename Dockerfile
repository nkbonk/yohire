# Dockerfile (корень проекта)
FROM python:3.11-slim

WORKDIR /app

# Сразу копируем только зависимостя, чтобы кешировать pip install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код (app/, alembic/, и т.п.)
COPY . .

# Запускаем uvicorn с autoreload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]