import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Floyd_Warshall_Algo import Floyd_Warshall


G = nx.DiGraph()
G.add_node('1', pos=(0, -100), name='1')
G.add_node('2', pos=(100, 0), name='2')
G.add_node('3', pos=(50, 100), name='3')
G.add_node('4', pos=(-100, 0), name='4')
# G.add_edges_from([('1', '3', weight = -2), ('3', '4', 2), ('4', '2', -1), ('2', '1', 4), ('2', '3', 3)])
G.add_edge('1', '3', weight=-2)
G.add_edge('3', '4', weight=2)
G.add_edge('4', '2', weight=-1)
G.add_edge('2', '1', weight=4)
G.add_edge('2', '3', weight=3)
node_map = ('1', '2', '3', '4')
table_data = np.zeros((node_map.__len__(), node_map.__len__()))

for row in range(table_data.__len__()):
    for col in range(table_data.__len__()):
        if G.has_edge(node_map[row], node_map[col]):
            u = node_map[col]
            v = node_map[row]
            if u != v:
                table_data[row][col] = G[v][u]["weight"]
                continue
        table_data[row][col] = np.inf
print(table_data)

T, parents = Floyd_Warshall(table_data)
print(parents)
print(T)

weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
# pos = nx.spring_layout(G)
name = nx.get_node_attributes(G, 'name')
nx.draw_networkx_nodes(G, pos, node_size=500, alpha=1)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', label=weight)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
plt.show()
