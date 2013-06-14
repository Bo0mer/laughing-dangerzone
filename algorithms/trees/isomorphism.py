from collections import defaultdict

from algorithms.trees.trees import _get_children
from exceptions.algoexceptions import NotUndirectedGraph


def _tuple_sort(tuples):
    ''' Sorts a list of tuples. '''
    l = len
    max_tuple_len = max(l(t) for t in tuples)
    buckets = [[] for _ in range(max_tuple_len)]

    for t in tuples:
        buckets[l(t)-1].append(t)

    tuples.clear()

    for bucket in buckets:
        bucket.sort()
        tuples.extend(bucket)


def _assign_level_labels(tree, root):
    ''' Assings labels to each node. Yeilds the different labels on
        each level of the tree. For more information, search for AHU
        algorithm for three isomorphism. '''

    labels = {u: 0 for u in tree if tree.degree(u) == 1 and u != root}
    children_labels = {}
    children, levels, height = _get_children(tree, root)
    sort = lambda x: tuple(sorted(x))  # helper

    for level in levels[:-1][::-1]:
        nodes_with_label = defaultdict(list)
        different_labels = set()

        for node in level:
            if node in children:  # if node has children
                for child in children[node]:  # for each children
                    if node in children_labels:
                        children_labels[node] += (labels[child],)
                    else:
                        children_labels[node] = (labels[child],)

                children_labels[node] = sort(children_labels[node])
                nodes_with_label[children_labels[node]].append(node)  # map the children labels to the node
                different_labels.add(children_labels[node])  # to compute different labels on the current level

        different_labels = list(different_labels)
        _tuple_sort(different_labels)

        yield different_labels

        for k, node_children_label in enumerate(different_labels):
            for node in nodes_with_label[node_children_label]:
                labels[node] = k  # k-th distinct tuple


def are_isomorphic(tree_one, root_one, tree_two, root_two):
    ''' Returns true if tree_one is isomorphic to tree_two,
        when rooting every tree in it's root '''

    if tree_one.is_directed() or tree_two.is_directed():
        raise NotUndirectedGraph("Trees must be undirected graphs!")

    t_one = _assign_level_labels(tree_one, root_one)
    t_two = _assign_level_labels(tree_two, root_two)  
    while True:
        try:
            if next(t_one) != next(t_two):
                return False
        except StopIteration:
            return True
