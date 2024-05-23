from fastapi import FastAPI, HTTPException
from .graph_manager import GraphManager
from .models import StartNode, MessageNode, ConditionNode, EndNode

app = FastAPI()
manager = GraphManager()

@app.post("/start_node")
def add_start_node(node: StartNode):
    manager.add_start_node(node)
    return {"message": "Start node added successfully"}

@app.post("/message_node")
def add_message_node(node: MessageNode):
    manager.add_message_node(node)
    return {"message": "Message node added successfully"}

@app.post("/condition_node")
def add_condition_node(node: ConditionNode):
    manager.add_condition_node(node)
    return {"message": "Condition node added successfully"}

@app.post("/end_node")
def add_end_node(node: EndNode):
    manager.add_end_node(node)
    return {"message": "End node added successfully"}

@app.get("/run_workflow/{start_node_id}/{end_node_id}")
def run_workflow(start_node_id: str, end_node_id: str):
    try:
        path = manager.find_path(start_node_id, end_node_id)
        return {"path": path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))