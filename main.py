from fastapi import FastAPI, HTTPException
from models import Node, Edge, WorkflowCreateRequest, WorkflowUpdateRequest, PathRequest, PathResponse
from graph_manager import GraphManager


app = FastAPI()
graph_manager = GraphManager()

@app.post("/workflow/create")
async def create_workflow(workflow_id: str, request: WorkflowCreateRequest):
    try:
        graph_manager.create_workflow(workflow_id, request.nodes, request.edges)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Workflow created successfully"}

@app.put("/workflow/update/{workflow_id}")
async def update_workflow(workflow_id: str, request: WorkflowUpdateRequest):
    try:
        graph_manager.update_workflow(workflow_id, request.nodes, request.edges)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Workflow updated successfully"}

@app.delete("/workflow/delete/{workflow_id}")
async def delete_workflow(workflow_id: str):
    try:
        graph_manager.delete_workflow(workflow_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Workflow deleted successfully"}

@app.post("/workflow/add_node/{workflow_id}")
async def add_node(workflow_id: str, node: Node):
    try:
        graph_manager.add_node(workflow_id, node)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Node added successfully"}

@app.post("/workflow/add_edge/{workflow_id}")
async def add_edge(workflow_id: str, edge: Edge):
    try:
        graph_manager.add_edge(workflow_id, edge)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Edge added successfully"}

@app.post("/workflow/path", response_model=PathResponse)
async def get_path(workflow_id: str, request: PathRequest):
    try:
        path = graph_manager.find_path(workflow_id, request.start_node, request.end_node)
        if path is None:
            raise HTTPException(status_code=404, detail="Path not found")
        return PathResponse(path=path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))