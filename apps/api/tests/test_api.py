from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root() -> None:
    """
    Test that the root endpoint returns successful health checks.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "name": "CyberNest API",
        "status": "healthy",
        "version": "1.0.0"
    }
