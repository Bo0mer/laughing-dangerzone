import unittest

from graphs.graphs import Graph
from algorithms.trees.center import centers


class CenterTest(unittest.TestCase):
    def setUp(self):
        self.tree_one = Graph()
        g = self.tree_one
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(4, 5)
        g.add_edge(4, 6)
        g.add_edge(3, 7)
        g.add_edge(3, 8)
        g.add_edge(7, 9)

        self.tree_two = Graph()
        g2 = self.tree_two
        g2.add_edge(1, 2)
        g2.add_edge(1, 3)
        g2.add_edge(1, 4)
        g2.add_edge(2, 7)
        g2.add_edge(2, 8)
        g2.add_edge(8, 9)
        g2.add_edge(3, 5)
        g2.add_edge(3, 6)

    def tearDown(self):
        del self.tree_one
        del self.tree_two

    def test_centers(self):
        self.assertEqual(centers(self.tree_one), {1, 3})
        self.assertEqual(centers(self.tree_two), {1, 2})
        tree = Graph()
        tree.add_edge(1, 2)
        tree.add_edge(2, 3)
        self.assertEqual(centers(tree), {2, })

    def test_centers_one_node_tree(self):
        tree = Graph()
        tree.add_node(1)
        self.assertEqual(centers(tree), {1, })

    def test_centers_empty_tree(self):
        tree = Graph()
        self.assertEqual(centers(tree), set())
