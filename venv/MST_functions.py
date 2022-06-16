# This file contains different algorithms to create the MST of a graph.
# MST - Minimal Spanning Tree, a tree that contains every vertex of the graph, and has the minimal sum of weights
# NOTE: every method must recieve a undirected weighted graph.
from disjoint_set import DisjointSet
from src.DiGraph import  DiGraph
from Graph_functions import create_undirected_graph
from BFS_Algorithm import connected_components
from create_nx_graph_from_DiGraph import create_nx_graph

def Reverse_kruskal(G):
    index = 0
    G = create_undirected_graph(G)
    T = DiGraph()
    edges = []
    for i in G.get_all_v():
        n = G.get_node(i)
        T.add_node(n.key, n.location)
        for dest, w in G.all_out_edges_of_node(i).items():
            edges.append(w)
            T.add_edge(dest,i,w)
    T = create_undirected_graph(T)
    create_nx_graph(T)
    edges.sort()
    index = len(edges) - 1
    for i in G.get_all_v():
        ok, cc = connected_components(T, i)
        break

    while ok == 1:
        for i in G.get_all_v():
            for dest, w in G.all_out_edges_of_node(i).items():
                if w == edges[index]:
                    T.remove_edge(i,dest)
                    T.remove_edge(dest, i)
                    ok, cc = connected_components(T, i)

                    index-=1
    return T