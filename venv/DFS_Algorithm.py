# The DFS algorithm (Depth first search) recieves a graph, scans it and returns raw data that uses different algorithms.
# The algorithm starts from a random vertex on the graph and uses recursion to traverse the graph.
# Complexity - O(|V|+|E|)
import numpy as np

def DFS(G):
    for n in G.get_all_v():
        node = G.get_node(n)
        node.tag = 0
        node.parent = 'start'
    time =0
    for n in G.get_all_v():
        if G.get_node(n).info == 'white':
            DFS_Visit(G, n, time)
    return

def DFS_Visit(G, u, time):
    time = time +1
    node = G.get_node(u)
    node.tag = time
    node.info = 'grey'
    for v, w in G.all_out_edges_of_node(u).items():
        if G.get_node(v).info == 'white':
            G.get_node(v).parent = u
            DFS_Visit(G, v, time)
    node.color = 'black'
    time+=1
    node.tag = time

