run:
	uvicorn app.main:app --reload

install:
	pip install -r requirements.txt

migrate:
	alembic upgrade head

postman:
	curl http://localhost:8000/openapi.json -o openapi.json
	openapi2postmanv2 -s openapi.json -o postman_collection.json -p

test:
	pytest -v --disable-warnings

VERSION := $(shell cat VERSION)

docker-build:
	docker build -t sre-student-api:$(VERSION) .

docker-run:
	docker run sre-student-api:$(VERSION)

docker: docker-build docker-run

up:
	docker-compose --env-file .env.local up --build

down:
	docker-compose down


