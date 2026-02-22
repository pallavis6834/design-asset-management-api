from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_assets_empty():
    response = client.get("/assets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
