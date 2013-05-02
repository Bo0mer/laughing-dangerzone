from algorithms.connectivity import is_connected


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