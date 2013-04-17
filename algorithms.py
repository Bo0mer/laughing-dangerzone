import copy
import heapq
from collections import deque, defaultdict

from graphs import Graph


def dfs(graph, start):
	''' Runs depth-first search from start node. yields (parent, child) for each visited node. '''
	if start in graph:
		stack = deque()
		visited = set()
		stack.append(start)
		while stack:
			node = stack.pop()
			visited.add(node)
			for adj_node in graph[node]:
				if adj_node not in visited:
					yield node, adj_node
					stack.append(adj_node)


def bfs(graph, start):
	''' Runs breadth-first serach from start node. yeilds {node: {child_node, child_node2},
	other_node: {o_child_node, o_child_node2}} '''
	current_level = [start]
	visited = {}
	while current_level:
		for node in current_level:
			visited[node] = 1
		next_level = set()
		level_graph = {node: set() for node in current_level}
		for node in current_level:
			for iter_node in graph[node]:
				if iter_node not in visited:
					level_graph[node].add(iter_node)
					next_level.add(iter_node)
		yield level_graph
		current_level = next_level


def connected_components(graph):
	''' Returns the number of connected components in undirected graph. '''
	if graph.is_directed():
		pass  # should be implemented later
	else:
		visited = set()
		components = 0
		for node in graph:
			if node not in visited:
				components += 1
				for parent, child in dfs(graph, node):
					visited.update([parent, child])
	return components


def is_connected(graph):
	return connected_components(graph) == 1


def unweighted_shortest_path(graph, start, end):
	''' Returns shortest path between start and end in list.
		If there is no path returns None. '''

	if start not in graph:
		return None
	visited = set()
	queue = deque([start])
	pred = {}
	while queue:
		current_node = queue.popleft()
		visited.add(current_node)
		for adj_node in graph[current_node]:
			if adj_node == end:
				reversed_path = [end, current_node]
				node_iter = copy.copy(current_node)
				while node_iter in pred:
					reversed_path.append(pred[node_iter])
					node_iter = pred[node_iter]
				return reversed_path[::-1]
			elif adj_node not in visited:
				queue.append(adj_node)
				pred[adj_node] = current_node


def shortest_paths_from(graph, start, pred=None, weight_attribute='weight'):
	''' Returns dict with shortest paths from start to each node,
		accessible from start. If pred (dict) is passed, 
		the predecessors for each node will be saved there. '''

	distance = {}
	distance[start] = 0
	if pred is not None:
		pred[start] = None
	for i in range(0, graph.order()):
		for u, distance_u in list(distance.items()):
			for v, data in graph[u].items():
				if v not in distance or distance[v] > distance_u + data[weight_attribute]:
					distance[v] = distance_u + data[weight_attribute]
					if pred is not None:
						pred[v] = u
	return distance


def pairs_of_shortest_paths(graph, weight_attribute='weight', infinity=65536):
	''' Computes all pairs of shortest paths in graph.
		Infinity should be specified, otherwise 65536 will be chosen.
		Returns dict with shortest paths, where dict[u][v] is the length
		of the shortest path between u and v, or infinity if there is no
		path between them. '''

	def edge_iter(graph):
		for node in graph:
			for other_node in graph[node]:
				yield node, other_node, graph[node][other_node]

	distance = {}
	for node in graph:
		distance[node] = defaultdict(lambda: infinity)
		distance[node][node] = 0

	for u, v, data in edge_iter(graph):
		distance[u][v] = data[weight_attribute]

	for u in graph:
		for v in graph:
			for w in graph:
				if distance[v][u] + distance[u][w] < distance[v][w]:
					distance[v][w] = distance[v][u] + distance[u][w]
	return dict(distance)


def dijkstra(graph, start, end=None, weight_attribute='weight'):
	distance = {}
	distance[start] = 0
	pred = {}
	pred[start] = None
	visited = set()
	heap = [(0, start)]

	for node in graph:
		if node != start:
			distance[node] = 65536
			heapq.heappush(heap, (65536, node))
	while heap:
		dist, current_node = heapq.heappop(heap)#

		if distance[current_node] == 65536:
			break

		for node in graph[current_node]:
			alt = dist + graph[current_node][node][weight_attribute]
			if alt < distance[node]:
				distance[node] = alt
				pred[node] = current_node
				heapq.heappush(heap, (alt, node))
	return distance
