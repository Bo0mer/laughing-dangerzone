def centers(tree):
    ''' Finds the center(s) of a tree. Note that
        tree might have one or two center(s)!!! '''
    last_removed = set()
    nodes_left = tree.order()
    center_degree = {}
    for v in tree:
        center_degree[v] = tree.degree(v)
        if tree.degree(v) <= 1:
            last_removed.add(v)
            nodes_left = nodes_left - 1
    while nodes_left:
        to_remove = set()
        for v in last_removed:
            for u in tree[v]:
                center_degree[u] = center_degree[u] - 1
                if center_degree[u] == 1:
                    to_remove.add(u)
                    nodes_left = nodes_left - 1
        last_removed = to_remove
    return last_removed
