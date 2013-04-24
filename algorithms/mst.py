import heapq


def mst_prim(graph, start=None, weight_attribute='weight'):
    ''' Yields (parent, child, weight) for each edge added
        to the minimum spanning tree. Note that there could
        be more than one such trees! Only for undirected graphs. '''

    if graph.is_directed():
        return None

    nodes = {node for node in graph if node != start}
    heap = []

    for v in graph[start]:
        heapq.heappush(heap, (graph[v][start][weight_attribute], start, v))

    while nodes:
        weight, u, v = heapq.heappop(heap)
        if v in nodes:
            nodes.discard(v)
            for w in graph[v]:
                if w in nodes:
                    heapq.heappush(heap,
                        (graph[v][w][weight_attribute], v, w))
            yield u, v, weight