from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Node(BaseModel):
    id: str
    type: Literal['start', 'message', 'condition', 'end']
    name: Optional[str] = None
    message_status: Optional[Literal['pending', 'sent', 'opened']] = None
    message_text: Optional[str] = None
    condition: Optional[bool] = None

class Edge(BaseModel):
    source: str
    target: str
    condition: Optional[Literal['yes', 'no']] = None

class WorkflowCreateRequest(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

class WorkflowUpdateRequest(BaseModel):
    nodes: Optional[List[Node]] = None
    edges: Optional[List[Edge]] = None

class PathRequest(BaseModel):
    start_node: str
    end_node: str

class PathResponse(BaseModel):
    path: List[str]

class WorkflowResponse(BaseModel):
    id: str
    nodes: List[Node]
    edges: List[Edge]