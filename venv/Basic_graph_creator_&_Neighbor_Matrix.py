import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('A', 'D')])

node_map = ('A', 'B', 'C', 'D')
table_data = np.identity(node_map.__len__())

for row in range(table_data.__len__()):
    for col in range(table_data.__len__()):
        if G.has_edge(node_map[col], node_map[row]):
            table_data[row][col] = 1
print(table_data)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()

def Floyd_Warshall(T):
    n=len(T)
    p = {}
    T_old = T
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if(T_old[i,j] > T_old[i,k] + T_old[k,j]):
                    T[i,j] = T_old[i,k] + T_old[k,j]
                    p[j,i] = k
        T_old = T
    return T, p


# def print_hi(name):
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
