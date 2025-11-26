from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_check():
    r = client.get("/health/")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert "healthy" in data["message"].lower()
