import networkx as nx
import matplotlib.pyplot as plt
from main import edge_list



G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

nx.draw(G, with_labels=True)
plt.show()