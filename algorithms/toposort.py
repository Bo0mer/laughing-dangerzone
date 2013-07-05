from exceptions.algoexceptions import NotDAG


def toposort(graph):
    ''' Returns list of nodes sorted in topological order. '''

    unvisited = {node for node in graph}
    temp_marked = set()
    sorted_order = []

    def visit(u):
        if u in temp_marked:
            raise NotDAG("Not a DAG!")
        if u in unvisited:
            temp_marked.add(u)
            for v in graph[u]:
                visit(v)
            temp_marked.discard(u)
            unvisited.discard(u)
            sorted_order.append(u)

    while unvisited:
        visit(list(unvisited)[0])
    return sorted_order[::-1]
