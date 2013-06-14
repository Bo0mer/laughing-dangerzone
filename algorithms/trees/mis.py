from collections import deque

from algorithms.traversal import bfs
from algorithms.trees.trees import _get_children


def max_independent_set(tree, root, weight_attribute='w'):
    ''' Finds the maximum independent set in rooted tree.
        The weight of every node is taken from each node's
        weight_attribute attribute. Returns (|MIS|, {MIS}),
        where |MIS| is the total weight of nodes in the
        set and {MIS} is the set of nodes. '''

    f_plus, f_minus = {}, {}
    max_set = set()
    children, levels, _ = _get_children(tree, root)
    weight = lambda u: tree.nodes[u][weight_attribute]

    for level in levels[::-1]:
        for u in level:
            if u in children:
                f_plus[u] = weight(u) + sum(f_minus[v]
                    for v in children[u])

                f_minus[u] = sum(max(f_plus[v], f_minus[v])
                    for v in children[u])
            else:
                f_plus[u], f_minus[u] = weight(u), 0

    def node_is_added(predecessor_is_added, node):
        return (not predecessor_is_added and
                f_plus[node] >= f_minus[node])

    stack = deque([(root, node_is_added(False, root))])
    while stack:
        u, added = stack.pop()
        if added:
            max_set.add(u)
        if u not in children:
            continue
        for v in children[u]:
            stack.append((v, node_is_added(added, v)))

    return max(f_plus[root], f_minus[root]), max_set
