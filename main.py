from fastapi import FastAPI, HTTPException
from models import Node, Edge


app = FastAPI()
workflows = {}

@app.get("/workflow/{workflow_id}")
async def get_workflow(workflow_id: int):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflows[workflow_id]

@app.post("/workflow/create")
async def create_workflow(workflow_id: int):
    if workflow_id in workflows:
        raise HTTPException(status_code=400, detail="Workflow already exists")
    workflows[workflow_id] = [Node(id="0", type='start')]

@app.put("/workflow/update/{workflow_id}")
async def update_workflow(workflow_id: int, node: Node):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    workflows[workflow_id].append(node)


@app.delete("/workflow/delete/{workflow_id}")
async def delete_workflow(workflow_id: int):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    del workflows[workflow_id]


@app.post("/workflow/add_node/{workflow_id}")
async def add_node(workflow_id: int, node: Node):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    workflows[workflow_id].append(node)


@app.post("/workflow/add_edge/{workflow_id}")
async def add_edge(workflow_id: int, edge: Edge):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    source_node = next((node for node in workflows[workflow_id] if node.id == edge.source), None)
    if source_node is None:
        raise HTTPException(status_code=400, detail="Source node not found")
    source_node.add_edge(edge)

@app.post("/workflow/path")
async def get_path(workflow_id: int, start_node_id: int, end_node_id: int):
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    # This is a placeholder. You'll need to implement a pathfinding algorithm here.
    return {"path": []}