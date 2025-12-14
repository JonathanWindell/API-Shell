from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_person():
    response = client.get("/person?count=1")
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 1
    assert "name" in data[0]
    assert "Deutsch" == data[0]["nationality"]