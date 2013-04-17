from collections import deque

from graphs import Graph


def dfs(graph, start):
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