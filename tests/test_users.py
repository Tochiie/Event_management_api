from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_get_update_delete_user():
    # Create user
    data = {"name": "Tochi", "email": "tochi@example.com"}
    res = client.post("/users/", json=data)
    assert res.status_code == 201
    user = res.json()
    user_id = user["id"]

    # Get user
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200
    assert res.json()["email"] == data["email"]

    # Update user
    updated = {"name": "Tochukwu"}
    res = client.put(f"/users/{user_id}", json=updated)
    assert res.status_code == 200
    assert res.json()["name"] == "Tochukwu"

    # Deactivate user
    res = client.put(f"/users/{user_id}/deactivate")
    assert res.status_code == 200

    # Delete user
    res = client.delete(f"/users/{user_id}")
    assert res.status_code == 204
