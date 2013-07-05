import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.max_path import *
from exceptions.algoexceptions import NegativeEdgeWeight, NotDAG


class MaxPathTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(1, 2)
        self.digraph = DiGraph()
        g = self.digraph
        g.add_edge(1, 3, w=3)
        g.add_edge(2, 3, w=5)
        g.add_edge(3, 5, w=11)
        g.add_edge(3, 4, w=8)
        g.add_edge(5, 6, w=12)
        g.add_edge(4, 7, w=16)
        g.add_edge(5, 7, w=14)
        g.add_edge(4, 6, w=18)
        g.add_edge(6, 8, w=21)
        g.add_edge(4, 7, w=16)
        g.add_edge(7, 8, w=16)
        g.add_edge(8, 10, w=7)
        g.add_edge(8, 9, w=5)

    def test_max_path(self):
        pred, distance = max_path(self.digraph, weight_attribute='w')
        self.assertEqual(59, max(distance.values()))
        self.assertEqual(pred,
                         {3: 2, 4: 3, 5: 3, 6: 4,
                          7: 5, 8: 6, 9: 8, 10: 8})

    def test_max_path_graph(self):
        with self.assertRaises(NotDAG):
            max_path(self.graph)

    def test_max_path_digraph_with_cycle(self):
        self.digraph.add_edge(10, 8, w=4)
        with self.assertRaises(NotDAG):
            max_path(self.digraph)
        self.digraph.remove_edge(10, 8)

    def test_max_path_negative_edge(self):
        self.digraph.add_edge(1, 1000, w=-1)
        with self.assertRaises(NegativeEdgeWeight):
            max_path(self.digraph, weight_attribute='w')
        self.digraph.remove_edge(1, 1000)
