import pytest
from fastapi.testclient import TestClient
from services.api.app.main import app

client = TestClient(app)

@pytest.fixture
def create_project():
    response = client.post("/api/v1/projects", json={"name": "Test Project"})
    assert response.status_code == 201
    return response.json()

def test_get_projects(create_project):
    response = client.get("/api/v1/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_project(create_project):
    project_id = create_project["id"]
    response = client.get(f"/api/v1/projects/{project_id}")
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_update_project(create_project):
    project_id = create_project["id"]
    response = client.patch(f"/api/v1/projects/{project_id}", json={"name": "Updated Project"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Project"

def test_delete_project(create_project):
    project_id = create_project["id"]
    response = client.delete(f"/api/v1/projects/{project_id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/projects/{project_id}")
    assert response.status_code == 404