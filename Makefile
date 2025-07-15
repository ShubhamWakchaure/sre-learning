# ---------------- CONFIG ----------------
DOCKER_USERNAME ?= your-docker-username
IMAGE_NAME ?= sre-student-api
VERSION := $(shell cat VERSION)
FULL_IMAGE_NAME := $(DOCKER_USERNAME)/$(IMAGE_NAME):$(VERSION)

PYTHON := python3
PIP := pip3

# ---------------- LOCAL DEV COMMANDS ----------------
run:
	uvicorn app.main:app --reload

install:
	$(PIP) install -r requirements.txt

migrate:
	alembic upgrade head

postman:
	curl http://localhost:8000/openapi.json -o openapi.json
	openapi2postmanv2 -s openapi.json -o postman_collection.json -p

# ---------------- QUALITY & TEST ----------------
test:
	pytest -v --disable-warnings

lint:
	flake8 app tests

# ---------------- DOCKER ----------------
docker-login:
	echo "$$DOCKER_PASSWORD" | docker login -u "$$DOCKER_USERNAME" --password-stdin

docker-build:
	docker build -t $(FULL_IMAGE_NAME) .

docker-push:
	docker push $(FULL_IMAGE_NAME)

docker: docker-build docker-run

up:
	docker-compose --env-file .env.local up --build

down:
	docker-compose down

# ---------------- CI MASTER STEP ----------------
ci: install lint test docker-login docker-build docker-push
	@echo "🎉 CI pipeline completed!"
