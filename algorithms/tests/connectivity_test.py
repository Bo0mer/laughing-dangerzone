import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.connectivity import *
from exceptions.algoexceptions import NotDiGraph, NotUndirectedGraph


class ConnectivityTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 2)
        g.add_edge(3, 4)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        self.digraph = DiGraph()
        dig = self.digraph
        dig.add_edge(1, 2)
        dig.add_edge(2, 3)
        dig.add_edge(3, 1)
        dig.add_edge(3, 4)
        dig.add_edge(4, 5)
        dig.add_edge(5, 4)
        dig.add_edge(5, 6)
        dig.add_edge(6, 7)
        dig.add_edge(7, 6)

    def tearDown(self):
        del self.graph
        del self.digraph

    def test_connected_components(self):
        self.assertEqual(
            list(connected_components(self.graph)),
            [{1, 2}, {3, 4}, {5, 6, 7}])

    def test_connected_components_digraph(self):
        with self.assertRaises(NotUndirectedGraph):
            list(connected_components(self.digraph))

    def test_strongly_connected_components(self):
        must_be = [{1, 2, 3}, {4, 5}, {6, 7}]
        sccs = strongly_connected_components(self.digraph)
        self.assertTrue(all(scc in sccs for scc in must_be))

    def test_strongly_connected_components_graph(self):
        with self.assertRaises(NotDiGraph):
            strongly_connected_components(self.graph)

    def test_number_connected_components(self):
        self.assertEqual(number_connected_components(self.graph), 3)
        self.assertEqual(number_connected_components(self.digraph), 3)

    def test_is_connected(self):
        self.assertFalse(is_connected(self.graph))
        self.assertFalse(is_connected(self.digraph))
