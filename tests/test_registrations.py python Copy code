from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_get_delete_registration():
    data = {
        "user_id": 1,
        "event_id": 1
    }

    res = client.post("/registrations/", json=data)
    assert res.status_code == 201
    reg = res.json()
    reg_id = reg["id"]

    res = client.get(f"/registrations/{reg_id}")
    assert res.status_code == 200

    res = client.delete(f"/registrations/{reg_id}")
    assert res.status_code == 204
