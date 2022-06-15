import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Floyd_Warshall_Algo import Floyd_Warshall
from src import DiGraph, GraphElements

def Create_simple_Binary_Tree():
    # simple Binary tree:
    G = DiGraph()
    n0 = NodeData(0, (0, 500, 0))
    n1 = NodeData(1, (50, 400, 0))
    n2 = NodeData(2, (-50, 400, 0))
    n3 = NodeData(3, (-100, 300, 0))
    n4 = NodeData(4, (-50, 300, 0))
    n5 = NodeData(5, (50, 300, 0))
    n6 = NodeData(6, (100, 300, 0))

    G.add_node(n0.key, n0.location)
    G.add_node(n1.key, n1.location)
    G.add_node(n2.key, n2.location)
    G.add_node(n3.key, n3.location)
    G.add_node(n4.key, n4.location)
    G.add_node(n5.key, n5.location)
    G.add_node(n6.key, n6.location)

    G.add_edge(0, 1, 0)
    G.add_edge(0, 2, 0)
    G.add_edge(1, 5, 0)
    G.add_edge(1, 6, 0)
    G.add_edge(2, 3, 0)
    G.add_edge(2, 4, 0)
    return G

def Create_Tree():
    # simple tree:
    G = DiGraph()
    n0 = NodeData(0, (0, 0, 0))
    n1 = NodeData(1, (50, 400, 0))
    n2 = NodeData(2, (-50, 400, 0))
    n3 = NodeData(3, (-100, 300, 0))
    n4 = NodeData(4, (-50, 300, 0))
    n5 = NodeData(5, (50, 300, 0))
    n6 = NodeData(6, (100, 300, 0))

    G.add_node(n0.key, n0.location)
    G.add_node(n1.key, n1.location)
    G.add_node(n2.key, n2.location)
    G.add_node(n3.key, n3.location)
    G.add_node(n4.key, n4.location)
    G.add_node(n5.key, n5.location)
    G.add_node(n6.key, n6.location)

    G.add_edge(0, 1, 0)
    G.add_edge(0, 2, 0)
    G.add_edge(1, 5, 0)
    G.add_edge(1, 6, 0)
    G.add_edge(2, 3, 0)
    G.add_edge(2, 4, 0)
    return G

