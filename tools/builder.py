from collections import deque
from itertools import islice, count

from graphs.graphs import Graph
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
