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
A = [[2, 1, -3, -4, 5],
     [0, 6, 3, 4, 1],
     [2, -2, -1, 4, -5],
     [-3, 3, 1, 0, 3]]
H, index, sum_ = Sub_Matrix_dp(A)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))
print(index)
print(sum_)
