import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_db
from app.models import Student

@pytest.fixture(autouse=True)
def clear_students():
    db = next(get_db())
    db.query(Student).delete()
    db.commit()

client = TestClient(app)

def test_healthcheck():
    res = client.get("/healthcheck")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_create_student():
    payload = {"name": "Test User", "email": "test@example.com", "status": "active"}
    res = client.post("/api/v1/students/", json=payload)
    assert res.status_code == 200
    assert res.json()["email"] == payload["email"]

def test_get_all_students():
    res = client.get("/api/v1/students/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_student_by_id():
    # First create a student
    payload = {"name": "ID User", "email": "id@example.com", "status": "active"}
    create = client.post("/api/v1/students/", json=payload)
    sid = create.json()["id"]

    # Now get the same student
    res = client.get(f"/api/v1/students/{sid}")
    assert res.status_code == 200
    assert res.json()["id"] == sid

def test_update_student():
    payload = {"name": "Old Name", "email": "old@example.com", "status": "active"}
    create = client.post("/api/v1/students/", json=payload)
    sid = create.json()["id"]

    # Update the student
    update = {"name": "Updated Name", "email": "updated@example.com", "status": "inactive"}
    res = client.put(f"/api/v1/students/{sid}", json=update)
    assert res.status_code == 200
    assert res.json()["name"] == "Updated Name"

def test_delete_student():
    payload = {"name": "Delete Me", "email": "delete@example.com", "status": "active"}
    create = client.post("/api/v1/students/", json=payload)
    sid = create.json()["id"]

    res = client.delete(f"/api/v1/students/{sid}")
    assert res.status_code == 200
    assert res.json()["message"] == "Student deleted"
