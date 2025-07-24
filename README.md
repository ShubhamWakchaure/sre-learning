## Student CRUD API Web server.

A simple student API server for managing student records (create, reda, update ,delete), built using fast api

Include:
- RESTFUL APIs versioned
- SQllte backend with alembic migrations
- Simple static UI
- Postman collection for testng
- Environment based configurations
- Dockerized application

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy + Alembic
- SQLite (for local testing)
- HTML/JS UI
- Pydantic
- Uvicorn
- Docker
- Nginx

## How to  Get Started

### Below tools are required for this project
1. make
2. docker desktop
3. Postman (Optional)

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
make up         # It will make the all the required containers up
make down       # It will Remove all the container,networks created earliers.
```

### 8. Python all the task command
System where make tool cannot be installed use the python task.py file do all the build, run and all 

### Notes
    1. You can direclty start , migrate, run  using make commands

## 🧬 OpenAPI Schema

The OpenAPI schema is available at: [localhost:8000/openapi.json](http://localhost:8000/openapi.json)

You can export it using:
```bash
curl http://localhost:8000/openapi.json -o postman_collecton.json
```


