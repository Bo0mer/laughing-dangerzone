import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.bipartiteness import *


class BipartitenessTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(1, 6)
        g.add_edge(3, 2)
        g.add_edge(3, 4)
        g.add_edge(3, 6)
        g.add_edge(5, 2)
        g.add_edge(5, 4)
        g.add_edge(5, 6)

    def tearDown(self):
        del self.graph

    def test_is_bipartite_graph(self):
        self.assertEqual(is_bipartite(self.graph),
            ({1, 3, 5}, {2, 4, 6}))

    def test_is_bipartite_not_bipartite_graph(self):
        self.graph.add_edge(1, 3)
        self.assertEqual(is_bipartite(self.graph), None)
        self.graph.remove_edge(1, 3)

    def test_is_balanced_bipartite(self):
        self.assertTrue(is_balanced_bipartite(self.graph))

    def test_is_balanced_bipartite_not_balanced(self):
        self.graph.add_edge(1, 100)
        self.assertFalse(is_balanced_bipartite(self.graph))
        self.graph.remove_edge(1, 100)

    def test_is_biregular(self):
        self.assertTrue(is_biregular(self.graph))

    def test_is_biregular_not_biregular_graph(self):
        self.graph.add_edge(1, 100)
        self.assertFalse(is_biregular(self.graph))
        self.graph.remove_edge(1, 100)