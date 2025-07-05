import os
import time
import platform
import psutil
import requests
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models
from app.db import get_db
import random

router = APIRouter(
    prefix="/api/v1/devops",
    tags=["devops-utils"]
)

# Record app start time for uptime metric
APP_START_TIME = time.time()

# Optional: safe env keys to expose
SAFE_ENV_KEYS = ["ENV", "APP_ENV", "DATABASE_URL", "BUILD_HASH", "LOG_LEVEL"]

def is_running_on_ec2():
    try:
        r = requests.get("http://169.254.169.254/latest/meta-data/instance-id", timeout=1)
        return r.status_code == 200
    except:
        return False


@router.get("/healthcheck")
def healthcheck():
    return {
        "status": "ok",
        "uptime_seconds": int(time.time() - APP_START_TIME),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }


@router.get("/info")
def app_info():
    return {
        "service": os.getenv("APP_NAME", "student-crud-api"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENV", "development"),
        "build_hash": os.getenv("BUILD_HASH", "n/a"),
        "ec2": is_running_on_ec2()
    }


@router.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    try:
        count = db.query(models.Student).count()
    except Exception:
        count = "unavailable"
    return {
        "total_students": count,
        "uptime_seconds": int(time.time() - APP_START_TIME),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_mb": round(psutil.virtual_memory().used / (1024 * 1024), 2)
    }


@router.get("/debug/env")
def env_dump():
    return {k: os.getenv(k) for k in SAFE_ENV_KEYS if os.getenv(k)}


@router.get("/routes", include_in_schema=False)
def list_routes(request: Request):
    return [
        {
            "path": route.path,
            "methods": list(route.methods),
            "name": route.name
        }
        for route in request.app.routes
    ]


@router.get("/simulate/error")
def simulate_error():
    raise HTTPException(status_code=500, detail="Simulated server error.")


@router.get("/simulate/timeout")
def simulate_timeout():
    time_sec =random.randint(0, 60)
    time.sleep(time_sec)
    return {"status": "delayed response", "seconds": time_sec}


@router.get("/system-info")
def system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu_cores": psutil.cpu_count(logical=True),
        "architecture": platform.machine(),
        "memory_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "hostname": platform.node()
    }


@router.get("/ec2/metadata")
def get_ec2_metadata():
    if not is_running_on_ec2():
        return {"error": "Not running on an EC2 instance"}

    base = "http://169.254.169.254/latest/meta-data/"
    keys = [
        "instance-id",
        "instance-type",
        "ami-id",
        "local-ipv4",
        "public-ipv4",
        "placement/availability-zone"
    ]
    metadata = {}
    for key in keys:
        try:
            r = requests.get(base + key, timeout=1)
            r.raise_for_status()
            metadata[key.replace("/", "_")] = r.text
        except Exception:
            metadata[key.replace("/", "_")] = "Unavailable"
    return metadata


@router.delete("/cleanup")
def cleanup_students(db: Session = Depends(get_db)):
    deleted = db.query(models.Student).delete()
    db.commit()
    return {"message": f"{deleted} student(s) deleted"}
