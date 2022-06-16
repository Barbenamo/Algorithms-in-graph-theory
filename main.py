import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue, PriorityQueue
import numpy as np
from disjoint_set import DisjointSet
from Floyd_Warshall_Algo import Floyd_Warshall
from Dijkstras_Shortest_Path_Algorithm import dijkstra
from src.DiGraph import DiGraph
from src.GraphElements import EdgeData
from src.GraphElements import NodeData
from create_nx_graph_from_DiGraph import create_nx_graph
import timeit
from Find_Graph_Diameter import best, diameter_dp, cycle_diameter_dp, cycle_best
from Build_Tree_From_Degrees_Array import build_tree
from Find_Max_Sub_Matrix import Sub_Matrix_dp
from BFS_Algorithm import BFS, connected_components
from DFS_Algorithm import DFS
from Bottle_Problem import Bottle_problem_matix_create, Bottle_problem
from Graph_functions import create_undirected_graph, is_directed, reverse, update_degrees,check_Euler_circle
from fire import fire
from MST_functions import Reverse_kruskal


# simple tree:
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

G.add_edge(0, 1, 1)
G.add_edge(0, 2, 2)
G.add_edge(1, 5, 3)
G.add_edge(1, 6, 4)
G.add_edge(2, 3, 5)
G.add_edge(2, 4, 6)
G.add_edge(0, 5, 6)
G.add_edge(5, 0, 6)
