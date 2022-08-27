# Algorithms-in-graph-theory
Various algorithms in graph theory.
### using original data structures, graphics by NetworkX and matplotlib.
Coded in phyton.

![Figure_1](https://user-images.githubusercontent.com/74831687/187038311-82d26046-b42a-4dc7-b6c7-fbfcdfb43aed.png)

Data-Structure:
=======
the data structure that the assignment is built on is a simple graph.
for info about this type of graph you can visit: [https://en.wikipedia.org/wiki/Graph_theory].
here are the classes of this data structure:
| class | description |
| ------|:-----------:|
| GraphElements| contains two classes, NodeData, which represents the vertex on the graph, and EdgeData, which represents the edge connecting two vertices. |
| DiGraph | this class contains various methods that can be used on the graph, such as adding/deleting a node, connects/disconnect vertices via edges etc. |

advanced algorithms.
==========================
here are some of the special methods:
----------------
* ```Dijkstras_Shortest_Path_Algorithm```: A method that calculates the shortest path between two given vertices, and retrievs a list of all the keys between them.
in order to calculate the shortest path between two given vertices on the graph, we used dijkstra's algorithm (DFS).<br />
for info about this specific algorithm please visit: [https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm].<br />
* ```create_nx_graph_from_DiGraph```: a method that uses the **matlibplot** library to plot and visualize the graph, showing it components-the vertices and the edges.
The method creates an NX graph using graph objects NetworkX graph from the GraphElements and DiGraph source objects.
* ```DFS_Algorithm```: depth-first-search, an algorithm that runs from a given source or a random one, and go through every node, iteretivly.
* ```Fire```: An algorithm that finds the root of a graph.
* ```Floyd_Warshall_Algo```: An FFF alogrithm that scans an weighted graph and returns a martrix describing the distance from each vertex to another.

