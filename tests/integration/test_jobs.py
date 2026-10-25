import pytest
from httpx import AsyncClient
from services.api.app.main import app

@pytest.mark.asyncio
async def test_create_job():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/projects/1/jobs", json={"video_url": "http://example.com/video.mp4"})
        assert response.status_code == 201
        assert "job_id" in response.json()

@pytest.mark.asyncio
async def test_get_job_status():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/jobs/1")
        assert response.status_code == 200
        assert response.json()["status"] in ["pending", "running", "completed", "failed"]

@pytest.mark.asyncio
async def test_cancel_job():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/jobs/1/cancel")
        assert response.status_code == 200
        assert response.json()["message"] == "Job cancelled successfully."

@pytest.mark.asyncio
async def test_retry_job():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/jobs/1/retry")
        assert response.status_code == 200
        assert response.json()["message"] == "Job retry initiated."