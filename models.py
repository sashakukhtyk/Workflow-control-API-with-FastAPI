from pydantic import BaseModel, Field
from typing import Optional, Literal, List, Union


class Edge(BaseModel):
    source: int
    target: int
    condition: Optional[Literal['yes', 'no']] = None

class Node(BaseModel):
    id: int
    type: Literal['start', 'message', 'condition', 'end']
    message_status: Optional[Literal['pending', 'sent', 'opened']] = None
    message_text: Optional[str] = None
    condition: Optional[bool] = None
    edges: Optional[List[Edge]] = Field(default_factory=list)

    def add_edge(self, edge: Edge):
        if self.type == 'start' and len(self.edges) > 0:
            raise ValueError("Start node can only have one target edge")
        if self.type == 'end' and edge.target is not None:
            raise ValueError("End node cannot have target edges")
        if self.type == 'message' and len([e for e in self.edges if e.target == edge.target]) > 0:
            raise ValueError("Message node can only have one target edge")
        if self.type == 'condition' and len(self.edges) > 1:
            raise ValueError("Condition node can only have two target edges")
        self.edges.append(edge)

class StartNode(Node):
    id: int
    type: Literal['start'] = 'start'

class MessageNode(Node):
    id: int
    type: Literal['message'] = 'message'
    message_status: Literal['pending', 'sent', 'opened']
    message_text: str

class ConditionNode(Node):
    id: int
    type: Literal['condition'] = 'condition'
    condition: bool

class EndNode(Node):
    id: int
    type: Literal['end'] = 'end'

