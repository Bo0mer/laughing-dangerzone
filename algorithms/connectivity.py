from collections import deque

from algorithms.traversal import bfs
from exceptions.algoexceptions import NotDiGraph, NotUndirectedGraph


def connected_components(graph):
    ''' Yields nodes in connected components one by one. '''

    if graph.is_directed():
        raise NotUndirectedGraph("Graph must be undirected!")

    visited = set()
    for node in graph:
        if node not in visited:
            component = {node, }
            for level_graph in bfs(graph, node):
                [component.update(level) for level in level_graph.values()]
            visited.update(component)
            yield component


def number_connected_components(graph):
    ''' Returns the number of (strongly)
    connected components in the graph. '''
    if graph.is_directed():
        return len(strongly_connected_components(graph))
    else:
        return len(list(connected_components(graph)))


def is_connected(graph):
    ''' Returns True if the graph is connected, e.g.
    has 1 (strongly) connected component. '''
    return number_connected_components(graph) == 1


def strongly_connected_components(graph):
    ''' Returns list of sets, with each connected component's
    nodes. Graph must be directed. '''

    if not graph.is_directed():
        raise NotDiGraph('Graph must be directed!')

    index = [0]
    indexes = {}
    low_level = {}
    stack = deque()
    set_stack = set()
    components = []

    def strongly_connect(v):
        indexes[v] = index[0]
        low_level[v] = index[0]
        index[0] = index[0] + 1
        stack.append(v)
        set_stack.add(v)
        for w in graph[v]:
            if w not in indexes:
                strongly_connect(w)
                low_level[v] = min(low_level[v], low_level[w])
            elif w in set_stack:
                low_level[v] = min(low_level[v], indexes[w])
        if low_level[v] == indexes[v]:
            scc = set()
            while True:
                w = stack.pop()
                set_stack.remove(w)
                scc.add(w)
                if w == v:
                    components.append(scc)
                    break

    for node in graph:
        if node not in indexes:
            strongly_connect(node)
    return components
