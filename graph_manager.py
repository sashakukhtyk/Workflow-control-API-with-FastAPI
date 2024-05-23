from typing import Dict
from models import StartNode, MessageNode, ConditionNode, EndNode, Node
import networkx as nx
from database import Base, Session, NodeModel, engine

class GraphManager:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def add_start_node(self, node: StartNode):
        # Create a new database node based on the StartNode object
        db_node = NodeModel(id=node.id, type=node.type, outgoing_edge=node.outgoing_edge)
        # Add the node to the session and commit the changes to the database
        self.session.add(db_node)
        self.session.commit()

    def add_message_node(self, node: MessageNode):
        # Create a new database node based on the MessageNode object
        db_node = NodeModel(id=node.id, type=node.type, outgoing_edge=node.outgoing_edge, 
                            message_text=node.message_text, status=node.status)
        # Add the node to the session and commit the changes to the database
        self.session.add(db_node)
        self.session.commit()

    def add_condition_node(self, node: ConditionNode):
        # Create a new database node based on the ConditionNode object
        db_node = NodeModel(id=node.id, type=node.type, condition=node.condition, 
                            yes_edge=node.yes_edge, no_edge=node.no_edge)
        # Add the node to the session and commit the changes to the database
        self.session.add(db_node)
        self.session.commit()

    def add_end_node(self, node: EndNode):
        # Create a new database node based on the EndNode object
        db_node = NodeModel(id=node.id, type=node.type)
        # Add the node to the session and commit the changes to the database
        self.session.add(db_node)
        self.session.commit()

    def build_graph(self):
        # Create a directed graph object
        G = nx.DiGraph()
        # Retrieve all nodes from the database
        nodes = self.session.query(NodeModel).all()
        for node in nodes:
            if node.type == "start" or node.type == "message":
                # Add an edge from the current node to its outgoing edge
                G.add_edge(node.id, node.outgoing_edge)
            elif node.type == "condition":
                # Add edges from the current node to its yes and no edges
                G.add_edge(node.id, node.yes_edge)
                G.add_edge(node.id, node.no_edge)
        return G

    def find_path(self, start_node_id: str, end_node_id: str):
        # Retrieve the start and end nodes from the database
        start_node = self.session.query(NodeModel).get(start_node_id)
        end_node = self.session.query(NodeModel).get(end_node_id)
        if not start_node or not end_node:
            # Raise an error if the start or end node is not found in the database
            raise ValueError("Start or end node not found in the database.")
        # Build the graph
        G = self.build_graph()
        try:
            # Find the shortest path between the start and end nodes
            path = nx.shortest_path(G, start_node_id, end_node_id)
        except nx.NetworkXNoPath:
            # Raise an error if no path is found between the start and end nodes
            raise ValueError("No path found between the start and end nodes.")
        return path