import unittest

from graphs.graphs import Graph
from algorithms.trees import *


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


    def test_rooted_tree_isomorphism(self):
        self.assertTrue(tree_isomorphism(self.tree_one, 1, self.tree_two, 1))

    def test_rooted_tree_no_isomorphism(self):
        self.assertFalse(tree_isomorphism(self.tree_one, 1, self.tree_two, 6))

    def test_unrooted_tree_isomorphism(self):
        self.assertTrue(
            unrooted_tree_isomorphism(self.tree_one, self.tree_two))

    def test_unrooted_tree_no_isomorphism(self):
        self.tree_two.add_edge(6, 666)
        self.assertFalse(
            unrooted_tree_isomorphism(self.tree_one, self.tree_two))
        self.tree_two.remove_edge(6, 666)

    def test_centers(self):
        self.assertEqual(centers(self.tree_one), {1, 3})
        self.assertEqual(centers(self.tree_two), {1, 2})
        tree = Graph()
        tree.add_edge(1, 2)
        tree.add_edge(2, 3)
        self.assertEqual(centers(tree), {2,})
