from collections import deque


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