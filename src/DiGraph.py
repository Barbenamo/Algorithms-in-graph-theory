from src.GraphElements import NodeData as ND
from src.GraphInterface import GraphInterface
import json


class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.graph = {}
        self.MC = 0
        self.numOfEdges = 0

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def v_size(self) -> int:
        return len(self.graph)

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def e_size(self) -> int:
        return self.numOfEdges

    """
    return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
    """

    def get_all_v(self) -> dict:
        return self.graph

    """
    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (key, weight)
     """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.graph.__contains__(id1):
            return self.graph.get(id1).guests
        return {}

    """
    return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
    weight)
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.graph.__contains__(id1):
            return self.graph.get(id1).neighbors
        return {}

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """

    def get_mc(self) -> int:
        return self.MC

    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """

    def add_edge(self, src: int, dest: int, w: float) -> bool:
        if not self.graph.__contains__(src) or not self.graph.__contains__(dest):
            return False
        if self.graph.get(src).has_nei(dest) or src == dest:
            return False
        self.graph.get(src).add_nei(dest, w)
        self.graph.get(dest).add_guest(src, w)
        self.numOfEdges += 1
        self.MC += 1
        return True

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    Note: if the node id already exists the node will not be added
    """

    def add_node(self, id: int, pos: tuple = None) -> bool:  # {"id" = id, "pos" = pos}
        if self.graph.__contains__(id):
            return False
        node = ND(id, pos)
        self.graph[id] = node
        self.MC += 1

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    Note: if the node id does not exists the function will do nothing
    """

    def remove_node(self, node_id: int) -> bool:
        if not self.graph.__contains__(node_id):
            return False
        neighbors = [key for key in self.graph.get(node_id).neighbors]
        guests = [key for key in self.graph.get(node_id).guests]
        for runner in neighbors:
            self.remove_edge(node_id, runner)
        for runner in guests:
            self.remove_edge(runner, node_id)
        self.graph.pop(node_id)
        self.MC += 1
        return True

    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.
    Note: If such an edge does not exists the function will do nothing
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.has_edge(node_id1, node_id2):
            return False
        self.graph.get(node_id1).remove_nei(node_id2)
        self.graph.get(node_id2).remove_guest(node_id1)
        self.MC += 1
        self.numOfEdges -= 1
        return True

    def has_edge(self, src: int, dest: int) -> bool:
        if not self.graph.__contains__(src) or not self.graph.__contains__(dest):
            return False
        if not self.graph.get(src).has_nei(dest):
            return False
        else:
            return True

    def get_node(self, key: int) -> ND:
        return self.graph.get(key)

    def has_node(self, key: int) -> bool:
        return self.graph.__contains__(key)

    def __str__(self):
        view_graph = self.as_dict()
        return view_graph.__str__()

    def __eq__(self, other):
        if not isinstance(other, DiGraph):
            return False
        if self.v_size() != other.v_size() or self.e_size() != other.v_size():
            return False
        for node in self.get_all_v().values():
            if node != other.get_node(node.key):
                return False
            edges = self.all_out_edges_of_node(node.key).items()
            other_edges = other.all_out_edges_of_node(node.key).items()
            if len(edges) != len(other_edges):
                return False
            if not edges.__eq__(other_edges):
                return False
        return True

    def as_dict(self) -> dict:
        nodes = []
        edges = []
        for runner in self.get_all_v().values():
            nodes.append(runner.node_info())
            my_edges = self.all_out_edges_of_node(runner.key)  # {"1": 5, "2": 4}
            for key, value in my_edges.items():  # {(1, 5), (2, 4)}
                edge_info = {"src": runner.key, "dest": key, "w": value}
                edges.append(edge_info)
        view_graph = {"Nodes": nodes, "Edges": edges}
        return view_graph

    def reset_color(self):
        for i in self.get_all_v():
            self.get_node(i).info = "white"
        return self
