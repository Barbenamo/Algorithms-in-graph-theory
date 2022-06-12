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
from Find_Graph_Diameter import diameter_dp
from Find_Graph_Diameter import best


G = DiGraph()
n0 = NodeData(0, (0, -100, 0))
n1 = NodeData(1, (100, 0, 0))
n2 = NodeData(2, (50, 100, 0))
n3 = NodeData(3, (-100, 0, 0))

G.add_node(n0.key, n0.location)
G.add_node(n1.key, n1.location)
G.add_node(n2.key, n2.location)
G.add_node(n3.key, n3.location)

G.add_edge(0, 1, 0)
G.add_edge(1, 2, 3)
G.add_edge(2, 3, 1)
G.add_edge(3, 0, 1)
G.add_edge(3, 1, 2)
# start = timeit.timeit()
# print(dijkstra(2, 1, G))
# end = timeit.timeit()
# print(end - start)
# start = timeit.timeit()
# create_nx_graph(G)
arr = (1, 7, 3, -13, 2, 1, 10, -2, 1, 20)
start = timeit.timeit()
mat, d, seq = diameter_dp(arr)
end = timeit.timeit()
print(end - start)
start = timeit.timeit()
print(best(arr))
end = timeit.timeit()
print(end - start)
print(mat)
print(d)
print(seq)
