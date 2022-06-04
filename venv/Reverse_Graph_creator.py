# This file contains a method to create a reverse graph from a given directed graph.
# reverse graph can be used for bidirectional Dijkstra algorithm for better run-time performence.
from src.DiGraph import DiGraph
from src.GraphElements import EdgeData
from src.GraphElements import NodeData


def Reverse(g):
    gr = DiGraph()
    for i in range(g.v_size()):
        n = g.get_node(i)
        s = n.get_key()
        t = n.get_location()
        gr.add_node(s, t)

    for i in range(g.v_size()):
        n = gr.get_node(i)
        s = n.get_key()
        for j in g.all_out_edges_of_node(i).items():
             gr.add_edge(j[0], s, j[1])
    return gr