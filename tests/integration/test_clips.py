import pytest
from httpx import AsyncClient
from services.api.app.main import app

@pytest.mark.asyncio
async def test_create_clip(client: AsyncClient):
    response = await client.post("/api/v1/projects/1/clips", json={
        "title": "Test Clip",
        "start_time": 10,
        "end_time": 20,
        "project_id": 1
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Clip"

@pytest.mark.asyncio
async def test_get_clips(client: AsyncClient):
    response = await client.get("/api/v1/projects/1/clips")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_render_clip(client: AsyncClient):
    response = await client.post("/api/v1/clips/1/render")
    assert response.status_code == 202
    assert "rendering" in response.json()["status"]

@pytest.mark.asyncio
async def test_download_clip(client: AsyncClient):
    response = await client.get("/api/v1/clips/1/download")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "video/mp4"