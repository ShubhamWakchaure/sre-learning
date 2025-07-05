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
