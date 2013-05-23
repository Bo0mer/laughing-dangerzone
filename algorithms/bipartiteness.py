from collections import deque

from algorithms.connectivity import is_connected


def _groupby(func, seq):
    result = {}
    for element in seq:
        result.setdefault(func(element), set()).add(element)
    return result


def is_bipartite(graph):
    ''' If graph is bipartite, returns two sets
        of nodes U and V, such that every edge
        is from a node in U to node in V. If not,
        returns None. Graph must be connected! '''

    if not is_connected(graph):
        return None
    start = next(graph.__iter__())
    black, red = True, False
    color = {start: black}
    stack = deque([start])
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if v not in color:
                color[v] = not color[u]
                stack.append(v)
            elif color[v] == color[u]:
                return None

    sets = _groupby(lambda x: color[x], color)
    return (sets[black], sets[red])


def is_balanced_bipartite(graph):
    ''' Returns true if graph is balanced bipartite. '''
    UV = is_bipartite(graph)
    if UV:
        return len(UV[0]) == len(UV[1])


def is_biregular(graph):
    ''' Returns true if graph is biregular. '''
    UV = is_bipartite(graph)
    if UV:
        degree = graph.degree
        for node_set in UV:
            rand_degree = degree(next(node_set.__iter__()))
            if any(degree(node) != rand_degree for node in node_set):
                return False
        return True
    return False
