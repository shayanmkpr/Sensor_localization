import numpy as np
import networkx as nx

def new_p_net(N):
    G = nx.grid_2d_graph(int(np.sqrt(N)), int(np.sqrt(N)), periodic=True)
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    return adjacency_matrix