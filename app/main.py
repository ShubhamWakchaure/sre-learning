from fastapi import FastAPI
from logging_config import setup_logging
from app.routers import students, devops_utils
from fastapi.staticfiles import StaticFiles
import time
import logging

logger = logging.getLogger(__name__)

setup_logging()
app = FastAPI(
    title="Student CRUD API",
    version="1.0.0"
)

# ✅ Register router BEFORE mount
app.include_router(students.router)
app.include_router(devops_utils.router)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/routes")
def list_routes():
    return [{"path": route.path, "name": route.name} for route in app.routes]


@app.get("/simulate/error")
def error():
    raise RuntimeError("Intentional test error")

@app.get("/simulate/timeout")
def timeout():
    time.sleep(10)
    return {"message": "delayed response"}


# ✅ Serve static frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
