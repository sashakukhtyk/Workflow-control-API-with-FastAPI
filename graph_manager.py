import networkx as nx
from models import Node, Edge
from typing import List

class GraphManager:
    def __init__(self):
        self.workflows = {}
    
    def create_workflow(self, workflow_id: str, nodes: List[Node], edges: List[Edge]):
        if workflow_id in self.workflows:
            raise ValueError("Workflow with this ID already exists.")
        self.workflows[workflow_id] = nx.DiGraph()
        self.node_data = {}
        for node in nodes:
            self.add_node(workflow_id, node)
        for edge in edges:
            self.add_edge(workflow_id, edge)
    
    def update_workflow(self, workflow_id: str, nodes: List[Node], edges: List[Edge]):
        if workflow_id not in self.workflows:
            raise ValueError("Workflow not found.")
        self.node_data = {node.id: node for node in nodes}
        for node in nodes:
            self.workflows[workflow_id].add_node(node.id, **node.dict())
        for edge in edges:
            self.workflows[workflow_id].add_edge(edge.source, edge.target, condition=edge.condition)
    
    def delete_workflow(self, workflow_id: str):
        if workflow_id in self.workflows:
            del self.workflows[workflow_id]
        else:
            raise ValueError("Workflow not found.")
    
    def add_node(self, workflow_id: str, node: Node):
        self.workflows[workflow_id].add_node(node.id, **node.dict())
        self.node_data[node.id] = node
    
    def add_edge(self, workflow_id: str, edge: Edge):
        source_type = self.node_data[edge.source].type
        target_type = self.node_data[edge.target].type
        
        if source_type == 'start':
            if len(list(self.workflows[workflow_id].successors(edge.source))) >= 1:
                raise ValueError("Start node can only have one outgoing edge.")
            if len(list(self.workflows[workflow_id].predecessors(edge.source))) > 0:
                raise ValueError("Start node cannot have incoming edges.")
        
        if source_type == 'message':
            if len(list(self.workflows[workflow_id].successors(edge.source))) >= 1:
                raise ValueError("Message node can only have one outgoing edge.")
        
        if source_type == 'condition':
            if edge.condition not in ['yes', 'no']:
                raise ValueError("Condition node must have 'yes' or 'no' edge.")
            if len([e for e in self.workflows[workflow_id].out_edges(edge.source, data=True) if e[2].get('condition') == edge.condition]) >= 1:
                raise ValueError("Condition node can only have one 'yes' and one 'no' edge.")
        
        if target_type == 'end':
            if len(list(self.workflows[workflow_id].successors(edge.target))) > 0:
                raise ValueError("End node cannot have outgoing edges.")
        
        self.workflows[workflow_id].add_edge(edge.source, edge.target, condition=edge.condition)
    
    def find_path(self, workflow_id: str, start_node: str, end_node: str):
        if workflow_id not in self.workflows:
            raise ValueError("Workflow not found.")
        try:
            path = nx.shortest_path(self.workflows[workflow_id], source=start_node, target=end_node)
            return path
        except nx.NetworkXNoPath:
            return None
