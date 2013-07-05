from algorithms.traversal import dfs


def base(graph):
    ''' Finds the base nodes of (un)directed graph. '''
    base_nodes = {node for node in graph}
    for node in graph:
        if node in base_nodes:
            for u, v in dfs(graph, node):
                base_nodes.discard(v)
    return base_nodes
