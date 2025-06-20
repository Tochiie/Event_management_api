from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_get_update_delete_speaker():
    data = {
        "name": "Adewale Yusuf",
        "topic": "Digital Health"
    }

    res = client.post("/speakers/", json=data)
    assert res.status_code == 201
    speaker = res.json()
    speaker_id = speaker["id"]

    res = client.get(f"/speakers/{speaker_id}")
    assert res.status_code == 200

    updated = {"name": "Jane AI"}
    res = client.put(f"/speakers/{speaker_id}", json=updated)
    assert res.status_code == 200
    assert res.json()["name"] == "Jane AI"

    res = client.delete(f"/speakers/{speaker_id}")
    assert res.status_code == 204
