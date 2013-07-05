import unittest

from graphs.graphs import Graph
from algorithms.trees.mis import max_independent_set


class MaxIndependentSetTest(unittest.TestCase):
    def setUp(self):
        tree = Graph()
        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(1, 4)
        tree.add_edge(2, 5)
        tree.add_edge(2, 6)
        tree.add_edge(5, 7)
        tree.add_edge(3, 8)
        tree.add_edge(4, 9)
        tree.add_edge(9, 10)
        self.tree = tree

    def tearDown(self):
        del self.tree

    def test_with_equal_nodes(self):
        for i in range(1, 11):
            self.tree.add_node(i, w=2)

        self.assertEqual(max_independent_set(self.tree, 1),
                        (10, {1, 5, 6, 8, 9}))

    def test_with_different_nodes(self):
        for i in range(1, 11):
            self.tree.add_node(i, w=i)

        self.assertEqual(max_independent_set(self.tree, 1),
                        (35, {4, 6, 7, 8, 10}))

    def test_with_one_and_only(self):
        t = Graph()
        t.add_node(1, p=1256)
        self.assertEqual(max_independent_set(t, 1, weight_attribute='p'),
                        (1256, {1, }))
