from typing import Dict
from .models import StartNode, MessageNode, ConditionNode, EndNode, Node
import networkx as nx

class GraphManager:
    def __init__(self):
        self.graph: Dict[str, Node] = {}

    def add_start_node(self, node: StartNode):
        self.graph[node.id] = node

    def add_message_node(self, node: MessageNode):
        self.graph[node.id] = node

    def add_condition_node(self, node: ConditionNode):
        self.graph[node.id] = node

    def add_end_node(self, node: EndNode):
        self.graph[node.id] = node

    def build_graph(self):
        G = nx.DiGraph()
        for node in self.graph.values():
            if node.type == "start" or node.type == "message":
                G.add_edge(node.id, node.outgoing_edge)
            elif node.type == "condition":
                G.add_edge(node.id, node.yes_edge)
                G.add_edge(node.id, node.no_edge)
        return G

    def find_path(self, start_node_id: str, end_node_id: str):
        G = self.build_graph()
        path = nx.shortest_path(G, start_node_id, end_node_id)
        return path