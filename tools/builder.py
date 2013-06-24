from collections import deque
from itertools import islice, count

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from exceptions.algoexceptions import InvalidDegreeSequence


def is_valid_degree_sequence(degree_sequence):
    ''' Returns True if the specified integer
        sequence is graphical. '''

    total_nodes = len(degree_sequence)

    if any(filter(lambda x: x > total_nodes, degree_sequence)):
        return False

    if any(filter(lambda x: x < 0, degree_sequence)):
        return False

    odd_degrees = sum(degree % 2 for degree in degree_sequence)
    if odd_degrees % 2 == 1:
        return False

    return True


def build_graph(degree_sequence, nodes=None):
    ''' Generates undirected graph of the given degree
        sequence. If nodes are provided, each node will
        have the corresponding data. '''

    if not is_valid_degree_sequence(degree_sequence):
        raise InvalidDegreeSequence('Invalid degree sequence!')

    graph = Graph()
    degree_node = []

    if not nodes:
        nodes = count()

    for item in map(lambda x, y: [x, y], degree_sequence, nodes):
        degree_node.append(item)

    degree_node.sort(reverse=True)
    degree_node = deque(degree_node)

    while degree_node:
        degree, node = degree_node.popleft()

        if degree == 0:
            graph.add_node(node)
            continue

        for other_dn in islice(degree_node, 0, degree):
            graph.add_edge(node, other_dn[1])
            other_dn[0] -= 1

    return graph


def _positive_order(degree_sequence):
    ''' Returns positive lexicographical ordering
        of degree_sequence. '''
    return sorted(degree_sequence, reverse=True)


def _check_positive_inequality(degree_sequence, k):
    ''' Checks Fulkerson theorem's inequality for specified k. '''
    lhs = 0
    for degree in degree_sequence[1:k+1]:
        lhs += min(degree[1], k-1)
    for degree in degree_sequence[k+1:]:
        lhs += min(degree[1], k)

    rhs = sum(degree[0] for degree in degree_sequence[1:k+1])

    return lhs >= rhs


def is_valid_directed_degree_sequence(degree_sequence):
    ''' Returns True if the specified degree sequence
        (out, in) is digraphical. '''

    pos_order = _positive_order(degree_sequence)
    n = len(degree_sequence) + 1

    if not all(_check_positive_inequality(pos_order, k)
                for k in range(n)):
        return False

    if (sum(deg[0] for deg in degree_sequence) !=
        sum(deg[1] for deg in degree_sequence)):
        return False

    return True


def build_digraph(degree_sequence, nodes=None):
    ''' Generates directed graph of the given degree
        sequence (out, in). If nodes are provided, each
        node will have the corresponding data. '''

    if not is_valid_directed_degree_sequence(degree_sequence):
        raise InvalidDegreeSequence('Invalid degree sequence!')

    graph = DiGraph()
    degree_node = []

    if not nodes:
        nodes = count()

    for item in map(lambda x, z: [x[0], x[1], z], degree_sequence, nodes):
        degree_node.append(item)

    degree_node.sort(key=lambda x: x[1], reverse=True)
    degree_node.sort(key=lambda x: x[0], reverse=True)

    degree_node = deque(degree_node)

    while degree_node:
        out_degree, in_degree, node = degree_node.popleft()

        if in_degree == out_degree == 0:
            graph.add_node(node)
            continue

        for out_in_node in degree_node:
            if out_degree == 0:
                break
            if out_in_node[1]:
                out_in_node[1] -= 1
                out_degree -= 1
                graph.add_edge(node, out_in_node[2])

        if in_degree:
            degree_node.append([out_degree, in_degree, node])

    return graph
