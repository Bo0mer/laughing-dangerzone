from algorithms.traversal import bfs


def connected_components(graph):
	''' Yields nodes in connected components one by one. '''

	if graph.is_directed():
		raise Exception("Graph must be undirected!")

	visited = set()
	for node in graph:
		if node not in visited:
			component = {node, }
			for level_graph in bfs(graph, node):
				[component.update(level) for level in level_graph.values()]
			visited.update(component)
			yield component


def number_connected_components(graph):
	''' Returns the number of connected components in the graph. '''
	return len(list(connected_components(graph)))


def is_connected(graph):
	''' Returns True if the graph is connected, e.g.
	 has 1 connected component. '''
	return number_connected_components(graph) == 1

