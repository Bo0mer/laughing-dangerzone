import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.eulerian import *
from exceptions.algoexceptions import NodeNotFound


class EulerianTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 9)
        g.add_edge(9, 6)
        g.add_edge(6, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(4, 3)
        g.add_edge(3, 2)
        g.add_edge(2, 8)
        g.add_edge(1, 8)
        g.add_edge(8, 5)
        g.add_edge(5, 7)
        g.add_edge(7, 8)
        self.digraph = DiGraph()
        dig = self.digraph
        dig.add_edge(1, 2)
        dig.add_edge(2, 5)
        dig.add_edge(2, 3)
        dig.add_edge(5, 3)
        dig.add_edge(3, 5)
        dig.add_edge(5, 6)
        dig.add_edge(6, 3)
        dig.add_edge(3, 4)
        dig.add_edge(4, 2)
        dig.add_edge(3, 7)
        dig.add_edge(7, 8)
        dig.add_edge(8, 1)

    def tearDown(self):
        del self.digraph
        del self.graph

    def test_is_eulerain_graph(self):
        self.assertTrue(is_eulerian(self.graph))

    def test_is_eulerian_digraph(self):
        self.assertTrue(is_eulerian(self.digraph))

    def test_find_eulerian_cycle_graph(self):
        self.assertEqual(find_eulerian_cycle(self.graph, 1),
                         [1, 8, 5, 7, 8, 2, 3, 4, 2, 1, 9, 6, 1])

    def test_find_eulerian_cycle_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            find_eulerian_cycle(self.graph, 999)

    def test_find_eulerian_cycle_not_eulerian_graph(self):
        self.graph.add_edge(101, 102)
        self.assertEqual(find_eulerian_cycle(self.graph, 1), None)
        self.graph.remove_edge(101, 102)

    def test_find_eulerian_cycle_digraph(self):
        self.assertEqual(find_eulerian_cycle(self.digraph, 1),
                         [1, 2, 3, 4, 2, 5, 3, 5, 6, 3, 7, 8, 1])

    def test_find_eulerian_cycle_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            find_eulerian_cycle(self.digraph, 999)

    def test_find_eulerian_cycle_not_eulerian_digraph(self):
        self.digraph.add_edge(101, 102)
        self.assertEqual(find_eulerian_cycle(self.digraph, 1), None)
        self.digraph.remove_edge(101, 102)
