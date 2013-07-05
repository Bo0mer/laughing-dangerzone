from algorithms.traversal import bfs
from algorithms.connectivity import is_connected


def is_tree(graph):
    ''' Returns whether graph is a tree.
        This implementation only allows
        undirected graphs! '''
    if is_connected(graph):
        if graph.order() == graph.size() + 1:
            return True
    return False


def _get_children(tree, root):
    ''' Returns dict(children), list(levels), int(height)
        children[v] contains all children of v in the tree
        rooted at root. levels contains lists of nodes on
        each level, starting from root. '''

    children = {}
    levels = []
    for i, level_tree in enumerate(bfs(tree, root)):
        levels.append([node for node in level_tree])
        for node in level_tree:
            if level_tree[node]:
                children[node] = list(level_tree[node])
    return children, levels, i
