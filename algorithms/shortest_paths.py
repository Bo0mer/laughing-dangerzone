import copy
import heapq
from collections import deque, defaultdict

from tools.edge_iter import edge_iter
from exceptions.algoexceptions import NegativeCycle, NodeNotFound
from algorithms.traversal import bfs


def unweighted_shortest_paths(graph, start, edge_weight=1):
    ''' Returns (predecessors, distance). predecessors[node]
    is the node's predecessor in the shortest path.
    distance[node] is the length of the path, where each
    crossed edge adds edge_weight=1 to the distance. '''

    if start not in graph:
        raise NodeNotFound(
            "Node {0} is not in the graph!".format(start))

    predecessors, distance = {start: None}, {start: 0}

    for level_graph in bfs(graph, start):
        for parent in level_graph:
            for child in level_graph[parent]:
                predecessors[child] = parent
                distance[child] = distance[parent] + edge_weight

    return (predecessors, distance)


def shortest_paths_from(graph, start, weight_attribute='weight'):
    ''' Returns (predecessors, distance). predecessors[node]
    is the predecessor of node in the shortest path,
    distance[node] is the shortest-path's lenght to node. No
    negative cycles allowed! '''

    if start not in graph:
        raise NodeNotFound(
            "Node {0} is not in the graph!".format(start))

    distance = {start: 0}
    predecessors = {start: None}
    for i in range(0, graph.order()):
        for u, distance_u in list(distance.items()):
            for v, data in graph[u].items():
                if v not in distance or distance[v] > distance_u + data[weight_attribute]:
                    distance[v] = distance_u + data[weight_attribute]
                    predecessors[v] = u
    for (u, v, attributes) in edge_iter(graph):
        if u in distance and v in distance:
            if distance[v] > distance[u] + attributes[weight_attribute]:
                raise NegativeCycle("Negative cycle found!")
    return (predecessors, distance)


def pairs_of_shortest_paths(graph, weight_attribute='weight', infinity=65536):
    ''' Computes all pairs of shortest paths in graph.
        Infinity should be specified, otherwise 65536 will be chosen.
        Returns dict with shortest paths, where dict[u][v] is the length
        of the shortest path between u and v, or infinity if there is no
        path between them. '''

    distance = {}
    for node in graph:
        distance[node] = defaultdict(lambda: infinity)
        distance[node][node] = 0

    for u, v, data in edge_iter(graph):
        distance[u][v] = data[weight_attribute]

    for u in graph:
        for v in graph:
            for w in graph:
                if distance[v][u] + distance[u][w] < distance[v][w]:
                    distance[v][w] = distance[v][u] + distance[u][w]
    return dict(distance)


def dijkstra(graph, start, weight_attribute='weight'):
    ''' Dijkstra's algorithm.
        Returns (predecessors, distance). predecessors[node]
        is the predecessor of node in the shortest path,
        distance[node] is the shortest-path's lenght to node.
        No negative edge-weights are allowed! '''

    if start not in graph:
        raise NodeNotFound(
            "Node {0} is not in the graph!".format(start))

    final_distance = {}
    distance = {start: 0}
    predecessors = {start: None}
    heap = [(0, start)]
    while heap:
        dv, v = heapq.heappop(heap)
        if v not in final_distance:
            final_distance[v] = dv
            for u in graph[v]:
                if u not in distance or distance[u] > dv + graph[v][u][weight_attribute]:
                    distance[u] = dv + graph[v][u][weight_attribute]
                    predecessors[u] = v
                    heapq.heappush(heap, (distance[u], u))
    return (predecessors, distance)