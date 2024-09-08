import pytest
import httpx

API_URL = "http://localhost:8000/api"
todo_id = "9999"

@pytest.fixture
def client():
    with httpx.Client(base_url=API_URL) as client:
        yield client

def test_get_todos(client):
    response = client.get(f"{API_URL}/get-all-notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_todo(client):
    data = {"id": todo_id, "task": 'This is a test to-do note', "done": False}
    response = client.post("/", json=data)
    assert response.status_code == 201
    todo = response.json()
    assert str(todo["id"]) == data["id"]
    assert todo["done"] == data["done"]
    # assert todo["task"] == data["task"]

def test_update_todo(client):
    update_to_do_id = "8888"
    # Create a new to-do note to update
    data = {"id": update_to_do_id, "task": 'This is a test to-do note', "done": False}
    create_response = client.post("/", json=data)
    assert create_response.status_code == 201
    todo_id = create_response.json()["id"]

    # Update the created to-do note
    update_data = {"task": 'This is a test UPDATED to-do note', "done": True}
    update_response = client.put(f"{API_URL}/{update_to_do_id}", json=update_data)
    assert update_response.status_code == 200
    updated_todo = update_response.json()
    assert str(updated_todo["id"]) == data["id"]
    assert updated_todo["done"] == update_data["done"]

def test_delete_todo(client):
    # Delete the created to-do note
    delete_response = client.delete(f"/{todo_id}")
    assert delete_response.status_code == 204

    # Verify the to-do note is deleted
    get_response = client.get(f"/{todo_id}")
    assert get_response.status_code == 405
