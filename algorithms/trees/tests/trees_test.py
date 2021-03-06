import unittest

from graphs.graphs import Graph
from algorithms.trees.trees import *


class TreesTest(unittest.TestCase):
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

    def test_is_tree(self):
        self.assertTrue(is_tree(self.tree_one))
        self.assertTrue(is_tree(self.tree_two))
        graph = Graph()
        graph.add_edge(1, 1)
        self.assertFalse(is_tree(graph))
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        self.assertFalse(is_tree(graph))
