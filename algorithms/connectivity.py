from algorithms.traversal import dfs


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