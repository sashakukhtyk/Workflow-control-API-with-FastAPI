import pytest
from models import StartNode, MessageNode, ConditionNode, EndNode
from graph_manager import GraphManager
from database import Base, NodeModel, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def graph_manager(db):
    return GraphManager()

def test_add_start_node(graph_manager, db):
    node = StartNode(id="start1", type="start", outgoing_edge="message1")
    graph_manager.add_start_node(node)
    db_node = db.query(NodeModel).get("start1")
    assert db_node is not None
    assert db_node.type == "start"
    assert db_node.outgoing_edge == "message1"

def test_add_message_node(graph_manager, db):
    node = MessageNode(id="message1", type="message", outgoing_edge="end1", 
                       message_text="Hello, world!", status="active")
    graph_manager.add_message_node(node)
    db_node = db.query(NodeModel).get("message1")
    assert db_node is not None
    assert db_node.type == "message"
    assert db_node.outgoing_edge == "end1"
    assert db_node.message_text == "Hello, world!"
    assert db_node.status == "active"

def test_add_condition_node(graph_manager, db):
    node = ConditionNode(id="condition1", type="condition", yes_edge="message1",
                         no_edge="end1", condition="x > 5")
    graph_manager.add_condition_node(node)
    db_node = db.query(NodeModel).get("condition1")
    assert db_node is not None
    assert db_node.type == "condition"
    assert db_node.yes_edge == "message1"
    assert db_node.no_edge == "end1"
    assert db_node.condition == "x > 5"

def test_add_end_node(graph_manager, db):
    node = EndNode(id="end1", type="end")
    graph_manager.add_end_node(node)
    db_node = db.query(NodeModel).get("end1")
    assert db_node is not None
    assert db_node.type == "end"


def test_build_graph(graph_manager, db):
    start_node = StartNode(id="start1", type="start", outgoing_edge="message1")
    message_node = MessageNode(id="message1", type="message", outgoing_edge="end1", 
                               message_text="Hello, world!", status="active")
    end_node = EndNode(id="end1", type="end")
    graph_manager.add_start_node(start_node)
    graph_manager.add_message_node(message_node)
    graph_manager.add_end_node(end_node)
    G = graph_manager.build_graph()
    assert len(G.nodes) == 3
    assert len(G.edges) == 2

def test_find_path(graph_manager, db):
    start_node = StartNode(id="start1", type="start", outgoing_edge="message1")
    message_node = MessageNode(id="message1", type="message", outgoing_edge="end1", 
                               message_text="Hello, world!", status="active")
    end_node = EndNode(id="end1", type="end")
    graph_manager.add_start_node(start_node)
    graph_manager.add_message_node(message_node)
    graph_manager.add_end_node(end_node)
    path = graph_manager.find_path("start1", "end1")
    assert path == ["start1", "message1", "end1"]