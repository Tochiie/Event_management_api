from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_events_empty_or_list():
    response = client.get("/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_get_update_delete_event():
    data = {"title": "Tech Hackathon", "location": "Lagos", "date": "2025-07-01", "description": "A Regional Tech Event"}
    resp = client.post("/events/", json=data)
    assert resp.status_code == 201
    event = resp.json()
    event_id = event["id"]

    resp = client.get(f"/events/{event_id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == data["title"]

    update = {"title": "Updated Event"}
    resp = client.put(f"/events/{event_id}", json=update)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Updated Event"

    resp = client.delete(f"/events/{event_id}")
    assert resp.status_code == 204

    resp = client.get(f"/events/{event_id}")
    assert resp.status_code == 404
