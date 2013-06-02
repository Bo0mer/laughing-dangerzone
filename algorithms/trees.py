from collections import deque

from algorithms.traversal import bfs
from algorithms.connectivity import is_connected


_LEFT, _RIGHT = '1', '0'

def is_tree(graph):
    ''' Returns whether graph is a tree.
        This implementation only allows 
        undirected graphs! '''
    if is_connected(graph):
        if graph.order() == graph.size() + 1:
            return True
    return False


def _sibling(graph, node):
    return next(iter(graph[node]))


def __root_canonical_name(tree, root):
    stack = deque([root])
    to_be_assigned = set()
    canonical_names = {}
    while stack:
        u = stack.pop()
        if u in to_be_assigned:
            u_label = ''.join(sorted(
                [canonical_names[v]
                for v in tree[u]
                if v not in to_be_assigned]))
            canonical_names[u] = _LEFT + u_label + _RIGHT
            to_be_assigned.discard(u)
        else:
            if tree.degree(u) == 1 and _sibling(tree, u) in to_be_assigned:
                canonical_names[u] = _LEFT + _RIGHT
            else:
                to_be_assigned.add(u)
                stack.append(u)
                [stack.append(v) for v in tree[u] if v not in to_be_assigned]
    return canonical_names[root]


def tree_isomorphism(tree_one, root_one, tree_two, root_two):
    ''' Returns whether rooted trees tree_one
        and tree_two are isomorphic. '''
    rcn_one = __root_canonical_name(tree_one, root_one)
    rcn_two = __root_canonical_name(tree_two, root_two)
    return rcn_one == rcn_two


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


def unrooted_tree_isomorphism(tree_one, tree_two):
    ''' Returns whether unrooted trees tree_one
        and tree_two are isomorphic. '''
    tone_centers = centers(tree_one)
    ttwo_centers = centers(tree_two)
    if len(tone_centers) == len(ttwo_centers) == 1:
        return tree_isomorphism(tree_one, list(tone_centers)[0],
                                tree_two, list(ttwo_centers)[0])
    if len(tone_centers) == len(ttwo_centers) == 2:
        p = tree_isomorphism(tree_one, list(tone_centers)[0],
                                tree_two, list(ttwo_centers)[0])
        q = tree_isomorphism(tree_one, list(tone_centers)[1],
                                tree_two, list(ttwo_centers)[0])
        return p or q
    return False