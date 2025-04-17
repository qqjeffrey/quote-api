from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_smoke_random_quote():
    response = client.get("/quote/random")
    assert response.status_code == 200

def test_get_by_author_not_found():
    response = client.get("/quote?author=NotExist")
    assert response.status_code == 200
    assert response.json() == []