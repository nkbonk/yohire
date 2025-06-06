# Основной запуск Docker Compose
up:
	docker compose up --build

# Остановка и удаление контейнеров
down:
	docker compose down

# Очистка зависимостей и билдов
clean:
	docker compose down -v --remove-orphans
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Тесты (если добавишь позже pytest)
test:
	docker compose exec web pytest

# Автоформатирование кода (исходя из твоих хуков)
lint:
	black .
	isort .
	flake8 .

# Pre-commit хуки вручную
hooks:
	pre-commit run --all-files

# Обновить зависимости
update-deps:
	pip install --upgrade -r requirements.txt

# Миграции через alembic
migrate:
	docker compose exec web alembic upgrade head
