import copy
import heapq
from collections import deque, defaultdict


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


def dijkstra(graph, start, pred=None, weight_attribute='weight'):
	''' Dijkstra's algorithm.
		Returns dict with shortest paths from start to each node,
		accessible from start. If pred (dict) is passed, 
		the predecessors for each node will be saved there.
		Dijkstra's algorithm WILL NOT work if there are edges
		with negative weight! '''

	distance = {start: 0}
	heap = [(0, start)]
	while heap:
		dv, v = heapq.heappop(heap)
		for u in graph[v]:
			if u not in distance:
				distance[u] = dv + graph[v][u][weight_attribute]
				heapq.heappush(heap, (distance[u], u))
			else:
				if distance[u] > dv + graph[v][u][weight_attribute]:
					distance[u] = dv + graph[v][u][weight_attribute]
			for w in graph[u]:
				alt = distance[u] + graph[u][w][weight_attribute]
				if w not in distance:
					heapq.heappush(heap, (alt, w))
				elif alt < distance[w]:
					distance[w] = alt
					if pred is not None:
						pred[w] = u
	return distance