import networkx as nx
import matplotlib.pyplot as plt
from Graph_functions import is_directed

# This method create a network x directed weighted graph out of a given Digraph object.
# mainly for illustrations.
def create_nx_graph(g):
    has_weights = False
    for i in g.get_all_v():
        n = g.get_node(i)
        for dest, w in g.all_out_edges_of_node(i).items():
            if w !=0:
                has_weights = True

    if is_directed(g):
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for i in range(g.v_size()):
        n = g.get_node(i)
        s = n.get_key()
        t = n.get_location()
        G.add_node(s, pos=(t[0], t[1]), name=s)
    for i in range(g.v_size()):
        n = g.get_node(i)
        s = n.get_key()
        for j in g.all_out_edges_of_node(i).items():
            G.add_edge(s, j[0], weight=j[1])

    if has_weights:
        weight = nx.get_edge_attributes(G, 'weight')
        pos = nx.get_node_attributes(G, 'pos')
        name = nx.get_node_attributes(G, 'name')
        nx.draw_networkx_nodes(G, pos, node_size=500, alpha=1)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', label=weight)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
        plt.show()
        return G
    else:
        pos = nx.get_node_attributes(G, 'pos')
        name = nx.get_node_attributes(G, 'name')
        nx.draw_networkx_nodes(G, pos, node_size=500, alpha=1)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()
        return G

