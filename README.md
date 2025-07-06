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
git clone https://github.com/your-username/sre-student-api.git
cd sre-student-api
```
### 2. Setup python virtual environment
- Windows

    ``` bash
    python -m venv .venv-sre-api
    source .venv\Scripts\activate.ps1
    ```
- Linux/Mac
    ``` bash
    python -m venv ..venv-sre-api
    source .venv/bin/activate 
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
```

### Notes
    1. You can direclty start , migrate, run  using mak commands

## 🧬 OpenAPI Schema

The OpenAPI schema is available at: [localhost:8000/openapi.json](http://localhost:8000/openapi.json)

You can export it using:
```bash
curl http://localhost:8000/openapi.json -o postman_collecton.json
