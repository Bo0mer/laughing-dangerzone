def edge_iter(graph):
        for node in graph:
            for other_node in graph[node]:
                yield node, other_node, graph[node][other_node]