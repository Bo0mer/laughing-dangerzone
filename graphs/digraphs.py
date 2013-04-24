

class DiGraph():

    def __init__(self, **kwargs):
        self.nodes = {}
        self.adjacent = {}
        self.predecessors = {}
        self.successors = self.adjacent
        self.attributes = {}
        if kwargs is not None:
            self.attributes.update(kwargs)

    def add_node(self, node, **kwargs):
        self.nodes.setdefault(node, {}).update(kwargs)
        if node not in self.adjacent:
            self.adjacent[node] = {}
            self.predecessors[node] = {}

    def remove_node(self, node):
        del self.nodes[node]
        for iter_node in self.adjacent:
            if node in self.adjacent[iter_node]:
                del self.adjacent[iter_node][node]
        for iter_node in self.predecessors:
            if node in self.predecessors[iter_node]:
                del self.predecessors[iter_node][node]
        del self.predecessors[node]
        del self.adjacent[node]

    def add_edge(self, u, v, **kwargs):
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)

        data = self.adjacent[u].setdefault(v, {})
        data.update(kwargs)
        self.successors[u][v] = data
        self.predecessors[v][u] = data

    def remove_edge(self, u, v):
        try:
            del self.successors[u][v]
            del self.predecessors[v][u]
        except KeyError:
            pass

    def has_edge(self, u, v):
        return v in self.successors[u]

    def get_predecessors(self, node):
        return iter(self.predecessors[node])

    def get_successors(self, node):
        return iter(self.successors[node])

    def __getitem__(self, key):
        return self.adjacent[key]

    def __iter__(self):
        return iter(self.nodes)

    def degree_iter(self):
        for node in self.nodes:
            yield node, self.degree(node)

    def is_directed(self):
        return True

    def order(self):
        return len(self.nodes)

    def size(self):
        return sum([degree for x, degree in self.degree_iter()])//2

    def in_degree(self, node):
        return len(self.predecessors[node])

    def out_degree(self, node):
        return len(self.adjacent[node])

    def degree(self, node):
        return self.out_degree(node) + self.in_degree(node)