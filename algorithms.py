from collections import deque

from graphs import Graph


def dfs(graph, start):
	''' Runs depth-first search from start node. yields (parent, child) for each visited node. '''
	if start in graph:
		stack = deque()
		visited = deque()
		stack.append(start)
		while stack:
			node = stack.pop()
			visited.appendleft(node)
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