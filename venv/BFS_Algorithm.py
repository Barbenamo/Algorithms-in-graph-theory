# This file contains the BFS algorithm, an algorithm that scans the graph by layers, and discover each node that can be
# reached from a given node named source.
# It also calculates the shortest path to each vertex.
# The algorithm works on non-direcet and directed graphs.
# WHITE - means that the vertex was not discoverd before.
# GREY - means that we discoverd it but did not attented it
# BLACK - means we already checked that node.

import numpy as np
from queue import Queue, PriorityQueue

def BFS(G, src):
    q = PriorityQueue()
    d = np.zeros(G.v_size())
    f = np.zeros(G.v_size())
    for i in G.get_all_v():
        n = G.get_node(i)
        d[i] = np.inf
        f[i] = None
    G.get_node(src).info = 'grey'
    d[src] = 0
    f[src] = None
    q.put(src)
    while not q.empty():
        u = q.get()
        for dest, w in G.all_out_edges_of_node(u).items():
            if G.get_node(dest).info == 'white':
                G.get_node(dest).info =  'grey'
                d[dest] = d[u] + w #for finding the weights
                f[dest] = u
                q.put(dest)
        G.get_node(dest).info = 'black'
    return d, f