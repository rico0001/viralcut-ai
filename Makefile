# Makefile

.PHONY: all build up down logs migrate test

all: build

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose exec api alembic upgrade head

test:
	docker-compose exec api pytest -v tests/