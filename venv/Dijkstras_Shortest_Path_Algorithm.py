from queue import Queue, PriorityQueue


def dijkstra(s, d, G):
    if not G.has_node(s) or not G.has_node(d):
        return None
    if s == d:
        return 0
    q = PriorityQueue()
    parents = {}
    node = G.get_node(s)
    node.weight = 0
    node.info = 'grey'
    q.put(node)
    while q:
        node = q.get()
        for dest, w in G.all_out_edges_of_node(node.key).items():
            weight = node.weight + w
            temp = G.get_node(dest)
            if temp.weight > weight and temp.info != "black":
                temp.weight = weight
                parents[temp.key] = node.key
                q.put(temp)
        node.info = "black"
        if node.key == d:
            s_path = []
            distance = node.weight
            key = d
            while key != s:
                s_path.insert(0, key)
                key = parents[key]
            s_path.insert(0, s)

            return distance, s_path
    for n in range(G.v_size()):
        G.get_node(n).info = 'white'
        # reset the info back to default
    return float('inf'), []
