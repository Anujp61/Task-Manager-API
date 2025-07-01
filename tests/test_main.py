from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Task Manager API"}

def test_create_task():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending"
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)