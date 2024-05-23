from pydantic import BaseModel
from typing import Optional, List

class Node(BaseModel):
    id: str

class StartNode(Node):
    type: str = "start"
    outgoing_edge: str

class MessageNode(Node):
    type: str = "message"
    status: str
    message_text: str
    outgoing_edge: str

class ConditionNode(Node):
    type: str = "condition"
    condition: str
    yes_edge: str
    no_edge: str

class EndNode(Node):
    type: str = "end"