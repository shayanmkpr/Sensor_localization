import networkx as nx
import numpy as np


def new_net(N):
    G = nx.connected_watts_strogatz_graph(N,4,p=2, seed=42)
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    adjacency_matrix = np.array(adjacency_matrix)
    np.fill_diagonal(adjacency_matrix, 1)
    nx.draw(G)
    return adjacency_matrix