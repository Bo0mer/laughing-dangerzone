

class Graph:

	def __init__(self, **kwargs):
		self.nodes = {}
		self.adjacent = {}
		self.attributes = {}
		if kwargs is not None:
			self.attributes.update(kwargs)

	def add_node(self, node, **kwargs):
		self.nodes.setdefault(node, {}).update(kwargs)
		if node not in self.adjacent:
			self.adjacent[node] = {}

	def remove_node(self, node):
		del self.adjacent[node]
		for iter_node in self.adjacent.keys():
			if node in self.adjacent[iter_node]:
				del self.adjacent[iter_node][node]
		del self.nodes[node]
	
	def add_edge(self, u, v, **kwargs):
		if u not in self.nodes:
			self.add_node(u)
			self.adjacent[u] = {}
		if v not in self.nodes:
			self.add_node(v)
			self.adjacent[v] = {}

		data = self.adjacent[u].setdefault(v, {})
		data.update(kwargs)
		self.adjacent[u][v] = data
		self.adjacent[v][u] = data

	def remove_edge(self, u, v):
		try:
			del self.adjacent[u][v]
			if u != v:
				del self.adjacent[v][u]
		except KeyError:
			pass

	def has_edge(self, u, v):
		try:
			return u in self.adjacent[v]
		except KeyError:
			return False

	def degree(self, node):
		if node in self.adjacent:
			return len(self.adjacent[node]) + (1 if node in self.adjacent[node] else 0)
		return 0

	def degree_iter(self):
		for node in self.nodes:
			yield node, self.degree(node)

	def is_directed(self):
		return False

	def __getitem__(self, value):
		return self.adjacent[value]

	def __iter__(self):
		return iter(self.nodes)

	def order(self):
		return len(self.nodes)

	def size(self):
		return sum([degree for x, degree in self.degree_iter()])//2

	def print_nodes(self):
		for node, node_attributes in self.nodes.items():
			print(node, node_attributes)




