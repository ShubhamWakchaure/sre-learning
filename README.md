## Student CRUD API Web server.

A simple student API server for mangang student records (create, red, update ,delete), bult usng fast api

Include:
- RESTFUL APIs versioned
- SQllte backend with alembic migrations
- Simple static UI
- Postman collection for testng
- Environment based configurations

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy + Alembic
- SQLite (for local testing)
- HTML/JS UI
- Pydantic
- Uvicorn

## How to  Get Started

### 1. Clone this repo

```bash
git clone https://github.com/ShubhamWakchaure/sre-student-api.git
cd sre-student-api
```
### 2. Setup python virtual environment
- Windows

    ``` bash
    python -m venv .venv-sre-api
    source .venv-sre-api\Scripts\activate.ps1
    ```
- Linux/Mac
    ``` bash
    python -m venv ..venv-sre-api
    source .venv-sre-api/bin/activate 
    ```

### 3. Install dependencies
``` bash
pip install -r requirements.txt
```

### 4. Setup the environment
``` 
cp .env.example .env.local
```
Note: Edit your DB connection string inside `.env.local`

### 4. Database migraton
Only for the first time
``` bash
alembic upgrade head
```

### 5. Run the server
``` bash
uvicorn app.main:app --reload
```

### 6. Check the browser and endpoint
    1. Open browser and go to this url: http://localhost:8000
    2. Docs can be accessed via this url: http://localhost:8000/docs

### 7. Makefile commands (Optional)
```bash
make run        # Run server
make migrate    # Run alembic upgrade
make test       # Run unit tests
make postman    # Create the json file required for postman 
make docker build & run # Build the docker image and runs the restapi webserver.
```

### 8. Python all the task command
System where make tooll cannot be installed use the python task.py file do all the build, run and all 

### Notes
    1. You can direclty start , migrate, run  using mak commands

## 🧬 OpenAPI Schema

The OpenAPI schema is available at: [localhost:8000/openapi.json](http://localhost:8000/openapi.json)

You can export it using:
```bash
curl http://localhost:8000/openapi.json -o postman_collecton.json
```


