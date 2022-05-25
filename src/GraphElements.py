class EdgeData:
    """A class which implements edges in the graph"""

    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = float("inf")
        self.info = "white"

    def __eq__(self, other) -> bool:
        if isinstance(other, EdgeData):
            if self.src == other.src and self.dest == other.dest and self.weight == other.weight:
                return True
        return False


class NodeData:
    """A class which represents data according to a vertex in the graph"""
    def __init__(self, key: int, location: tuple = None):
        self.key = key
        self.location = tuple(location)
        self.parent = None
        self.weight = float("inf")
        self.tag = -1
        self.info = "white"
        self.neighbors = {}
        self.guests = {}

    def add_nei(self, dest: int, weight: float):
        if self.has_nei(dest):
            return
        self.neighbors[dest] = weight

    def add_guest(self, src: int, weight: float):
        if self.has_guest(src):
            return
        self.guests[src] = weight

    def remove_nei(self, key: int):
        if self.has_nei(key):
            self.neighbors.pop(key)

    def remove_guest(self, key: int):
        if self.has_guest(key):
            self.guests.pop(key)

    def has_nei(self, key: int) -> bool:
        return self.neighbors.__contains__(key)

    def has_guest(self, key: int) -> bool:
        return self.guests.__contains__(key)

    def __eq__(self, other):
        if isinstance(other, NodeData):
            if self.key == other.key and self.location == other.location:
                return True
        return False

    def __repr__(self):
        node_info = {"id": self.key, "pos": self.location}
        return node_info.__str__()

    def node_info(self) -> dict:
        return {"id": self.key, "pos": self.location}

    def __lt__(self, other):
        return self.weight < other.weight
