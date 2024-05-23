from fastapi.testclient import TestClient
import pytest
from main import app, manager
from models import StartNode, MessageNode, EndNode

client = TestClient(app)

def test_workflow():
    # Add nodes
    start_node = StartNode(id="start", outgoing_edge="message")
    message_node = MessageNode(id="message", status="active", message_text="Hello, World!", outgoing_edge="end")
    end_node = EndNode(id="end")

    client.post("/start_node", json=start_node.dict())
    client.post("/message_node", json=message_node.dict())
    client.post("/end_node", json=end_node.dict())

    # Run workflow
    response = client.get("/run_workflow/start/end")
    assert response.status_code == 200
    assert response.json() == {"path": ["start", "message", "end"]}

    # Cleanup
    manager.graph.clear()

@pytest.fixture(autouse=True)
def run_around_tests():
    # Before each test, clear the graph
    yield
    # After each test, clear the graph
    manager.graph.clear()