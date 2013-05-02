import copy
import heapq
from collections import deque, defaultdict

from tools.edge_iter import edge_iter
from exceptions.algoexceptions import NegativeCycle, NodeNotFound


def unweighted_shortest_path(graph, start, end):
    ''' Returns shortest path between start and end in list.
        If there is no path returns None. '''

    if start not in graph:
        raise NodeNotFound(
            "Node {0} is not in the graph!".format(start))
    
    visited = set()
    queue = deque([start])
    pred = {}
    while queue:
        current_node = queue.popleft()
        visited.add(current_node)
        for adj_node in graph[current_node]:
            if adj_node == end:
                reversed_path = [end, current_node]
                node_iter = copy.copy(current_node)
                while node_iter in pred:
                    reversed_path.append(pred[node_iter])
                    node_iter = pred[node_iter]
                return reversed_path[::-1]
            elif adj_node not in visited:
                queue.append(adj_node)
                pred[adj_node] = current_node


def shortest_paths_from(graph, start, weight_attribute='weight'):
    ''' Returns dict with shortest paths from start to each node,
        accessible from start. If pred (dict) is passed, 
        the predecessors for each node will be saved there. '''

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
        Returns dict with shortest paths from start to each node,
        accessible from start. If pred (dict) is passed, 
        the predecessors for each node will be saved there.
        Dijkstra's algorithm WILL NOT work if there are edges
        with negative weight! '''

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