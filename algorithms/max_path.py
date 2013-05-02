from collections import deque

from algorithms.toposort import toposort
from exceptions.algoexceptions import NegativeEdgeWeight


def max_path(graph, weight_attribute='weight'):
    """ Finds all max-paths within DAG with NO NEGATIVE WEIGHTS.
        Returns two dicts - distance, predecessor. distance[node]
        is the max-path's length, predecessor[node] is the node's
        predecessor in the max-path. """

    toposort(graph)

    distance = {node: 0 for node in graph}
    predecessors = {}

    def visit(node):
        stack = deque([node])
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if graph[u][v][weight_attribute] < 0:
                    raise NegativeEdgeWeight('Negative edge weight found!')
                if distance[v] < distance[u] + graph[u][v][weight_attribute]:
                    distance[v] = distance[u] + graph[u][v][weight_attribute]
                    predecessors[v] = u
                stack.append(v)

    for node in graph:
        if distance[node] == 0:
            visit(node)
    return (predecessors, distance)