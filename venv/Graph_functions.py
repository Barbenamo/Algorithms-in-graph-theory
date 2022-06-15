# This file contains methods that recieve the Digraph graph objects and returns different graphs.
from src.DiGraph import DiGraph
from src.GraphElements import EdgeData
from src.GraphElements import NodeData

# Checks wheter the graph is directed or not
def is_directed(G) -> bool:
    for i in G.get_all_v():
        n = G.get_node(i)
        for dest, w in G.all_out_edges_of_node(i).items():
            if not G.has_edge(dest , i):
                return True
    return False

# Creates a undirected graph out of a graph
def create_undirected_graph(G):
    gu = DiGraph()
    for i in range(G.v_size()): # add each node in g to gr
        n = G.get_node(i)
        s = n.get_key()
        t = n.get_location()
        gu.add_node(s, t)

    for i in range(G.v_size()):# add two edges
        n = gu.get_node(i)
        s = n.get_key()
        for dest, w in G.all_out_edges_of_node(i).items():
             gu.add_edge(s, dest, w)
             gu.add_edge(dest, s, w)
    return gu

# Flip every edge direction
def reverse(g):
    if not is_directed(g):
        print('This graph is not directed')
        return None
    gr = DiGraph() #initialize graph
    for i in range(g.v_size()): # add each node in g to gr
        n = g.get_node(i)
        s = n.get_key()
        t = n.get_location()
        gr.add_node(s, t)

    for i in range(g.v_size()):# add the reverse edge between each two connected nodes
        n = gr.get_node(i)
        s = n.get_key()
        for j in g.all_out_edges_of_node(i).items():
             gr.add_edge(j[0], s, j[1])
    return gr
# This method updates each degree of vertex in graph G using the tag and neighbors
def update_degrees(G):
    for i in G.get_all_v():
        n = G.get_node(i)
        n.tag = len(n.neighbors) + len(n.guests)
    return