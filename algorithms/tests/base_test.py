import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.base import base


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 2)
        g.add_edge(2, 5)
        g.add_edge(7, 8)
        g.add_node(11)
        self.digraph = DiGraph()
        dig = self.digraph
        dig.add_edge(1, 2)
        dig.add_edge(2, 3)
        dig.add_edge(3, 4)
        dig.add_edge(4, 1)
        dig.add_edge(7, 3)
        dig.add_edge(8, 9)
        dig.add_node(6)

    def tearDown(self):
        del self.graph
        del self.digraph

    def test_base_graph(self):
        graph_base = base(self.graph)
        self.assertTrue(any([node in graph_base for node in {1, 2, 5}]))
        self.assertTrue(any([7 in graph_base, 8 in graph_base]))
        self.assertTrue(11 in graph_base)
        self.assertEqual(len(graph_base), 3)

    def test_base_digraph(self):
        digraph_base = base(self.digraph)
        self.assertEqual({6, 7, 8}, digraph_base)
