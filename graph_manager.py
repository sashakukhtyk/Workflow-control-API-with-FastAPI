from typing import Dict
from models import StartNode, MessageNode, ConditionNode, EndNode, Node
import networkx as nx
from database import Base, Session, NodeModel, engine

class GraphManager:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def add_start_node(self, node: StartNode):
        db_node = NodeModel(id=node.id, type=node.type, outgoing_edge=node.outgoing_edge)
        self.session.add(db_node)
        self.session.commit()

    def add_message_node(self, node: MessageNode):
        db_node = NodeModel(id=node.id, type=node.type, outgoing_edge=node.outgoing_edge, 
                            message_text=node.message_text, status=node.status)
        self.session.add(db_node)
        self.session.commit()

    def add_condition_node(self, node: ConditionNode):
        db_node = NodeModel(id=node.id, type=node.type, condition=node.condition, 
                            yes_edge=node.yes_edge, no_edge=node.no_edge)
        self.session.add(db_node)
        self.session.commit()

    def add_end_node(self, node: EndNode):
        db_node = NodeModel(id=node.id, type=node.type)
        self.session.add(db_node)
        self.session.commit()

    def build_graph(self):
        G = nx.DiGraph()
        nodes = self.session.query(NodeModel).all()
        for node in nodes:
            if node.type == "start" or node.type == "message":
                G.add_edge(node.id, node.outgoing_edge)
            elif node.type == "condition":
                G.add_edge(node.id, node.yes_edge)
                G.add_edge(node.id, node.no_edge)
        return G

    def find_path(self, start_node_id: str, end_node_id: str):
        start_node = self.session.query(NodeModel).get(start_node_id)
        end_node = self.session.query(NodeModel).get(end_node_id)
        if not start_node or not end_node:
            raise ValueError("Start or end node not found in the database.")
        G = self.build_graph()
        try:
            path = nx.shortest_path(G, start_node_id, end_node_id)
        except nx.NetworkXNoPath:
            raise ValueError("No path found between the start and end nodes.")
        return path