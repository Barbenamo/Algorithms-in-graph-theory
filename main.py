import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue, PriorityQueue
import numpy as np
from Floyd_Warshall_Algo import Floyd_Warshall
from Dijkstras_Shortest_Path_Algorithm import dijkstra
from src.DiGraph import DiGraph
from src.GraphElements import EdgeData
from src.GraphElements import NodeData
from create_nx_graph_from_DiGraph import create_nx_graph
from Reverse_Graph_creator import Reverse
import timeit
from Find_Graph_Diameter import best, diameter_dp, cycle_diameter_dp, cycle_best
from Build_Tree_From_Degrees_Array import build_tree
from Find_Max_Sub_Matrix import Sub_Matrix_dp
from BFS_Algorithm import BFS, connected_components

G = DiGraph()
n0 = NodeData(0, (0, -100, 0))
n1 = NodeData(1, (100, 0, 0))
n2 = NodeData(2, (50, 100, 0))
n3 = NodeData(3, (-100, 0, 0))
n4 = NodeData(4, (-50, 300, 0))
n5 = NodeData(5, (30, 500, 0))
n6 = NodeData(6, (500, 500, 0))


G.add_node(n0.key, n0.location)
G.add_node(n1.key, n1.location)
G.add_node(n2.key, n2.location)
G.add_node(n3.key, n3.location)
G.add_node(n4.key, n4.location)
G.add_node(n5.key, n5.location)
G.add_node(n6.key, n6.location)


G.add_edge(0, 1, 0)
G.add_edge(1, 2, 3)
G.add_edge(2, 3, 1)
G.add_edge(3, 0, 1)
G.add_edge(3, 1, 2)

G.add_edge(4, 5, 1)
G.add_edge(5, 6, 2)
G.add_edge(6, 4, 3)
d, f = BFS(G, 0)
print(d)
print(f)
count = connected_components(G, 0)
print(count)
create_nx_graph(G)

