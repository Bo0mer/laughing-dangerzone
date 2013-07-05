import unittest

from graphs.graphs import Graph
from algorithms.trees.isomorphism import are_isomorphic


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

    def test_are_isomorphic(self):
        self.assertTrue(are_isomorphic(
                        self.tree_one, 1,
                        self.tree_two, 1))

    def test_are_isomorphic_false(self):
        self.assertFalse(are_isomorphic(
            self.tree_one, 1,
            self.tree_two, 3))
