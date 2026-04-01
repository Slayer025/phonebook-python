from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# CREATE
def test_create_contact():
    response = client.post("/contacts/", json={
        "name": "John Doe",
        "phone_number": "+919999999999",
        "email": "john@example.com",
        "address": "Mumbai"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


# GET ALL
def test_get_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200


# GET ONE
def test_get_contact():
    response = client.get("/contacts/1")
    assert response.status_code in [200, 404]


# UPDATE
def test_update_contact():
    response = client.put("/contacts/1", json={
        "name": "Updated Name",
        "phone_number": "+918888888888",
        "email": "updated@example.com",
        "address": "Delhi"
    })
    assert response.status_code in [200, 404]


# DELETE
def test_delete_contact():
    response = client.delete("/contacts/1")
    assert response.status_code in [200, 404]