import queue
from create_nx_graph_from_DiGraph import create_nx_graph
from Graph_functions import update_degrees

# This method returns the graph diameter - which is the largest distance between two vertices.
# NOTE: this method changes the graph!

def fire(G):
    count = 0
    q = queue.Queue()
    while(G.v_size()>=2):
        create_nx_graph(G)
        for i in G.get_all_v():
            n = G.get_node(i)
            if n.tag ==1:
                q.put(i)
        count +=1
        while not q.empty():
            G.remove_node(q._get())

        update_degrees(G)
    if G.v_size() == 2:
        return 2*count + 1
    return 2*count