from collections import deque

from algorithms.connectivity import is_connected
from exceptions.algoexceptions import NodeNotFound


def is_eulerian(graph):
    """ Returns True if the graph is Eulerian. """

    if graph.is_directed():
        if is_connected(graph):
            return all((
                graph.in_degree(node) == graph.out_degree(node)
                for node in graph))
    else:
        if is_connected(graph):
            return all((
                graph.degree(node) % 2 == 0
                for node in graph))
    return False


def find_eulerian_cycle(graph, start):
    ''' Tries to find Eulerian cycle in the graph, starting
    from start. If there isn't such, None is returned, else
    returns list with following nodes from the cycle. '''

    if not is_eulerian(graph):
        return None

    if start not in graph:
        raise NodeNotFound(
            'Node {0} is not in the graph!'.format(start))

    used_edges = set()
    recursion_stack, reversed_path = deque([start]), []
    while recursion_stack:
        u = recursion_stack[-1]
        for v in graph[u]:
            if (u, v) not in used_edges:
                recursion_stack.append(v)
                used_edges.add((u, v))
                if not graph.is_directed():
                    used_edges.add((v, u))
                break
        else:
            recursion_stack.pop()
            reversed_path.append(u)

    return reversed_path[::-1]