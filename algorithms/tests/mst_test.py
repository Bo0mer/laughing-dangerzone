import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.mst import mst_prim
from exceptions.algoexceptions import NotUndirectedGraph, NodeNotFound


class MSTTest(unittest.TestCase):
    def setUp(self):
        self.digraph = DiGraph()
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 2, weight=3)
        g.add_edge(2, 3, weight=10)
        g.add_edge(3, 4, weight=15)
        g.add_edge(3, 6, weight=7)
        g.add_edge(6, 5, weight=9)
        g.add_edge(6, 7, weight=12)
        g.add_edge(6, 8, weight=5)
        g.add_edge(7, 8, weight=6)
        g.add_edge(8, 1, weight=14)
        g.add_edge(8, 2, weight=8)

    def tearDown(self):
        del self.graph
        del self.digraph

    def test_mst_prim_sum(self):
        for i in range(1, 9):
            self.assertEqual(
                sum([weight for u, v, weight in mst_prim(self.graph, i)]),
                53)

    def test_mst_prim_tree(self):
        self.assertEqual(list(mst_prim(self.graph, 1)),
                [(1, 2, 3), (2, 8, 8), (8, 6, 5),
                 (8, 7, 6), (6, 3, 7), (6, 5, 9), 
                 (3, 4, 15)])

    def test_mst_prim_digraph(self):
        with self.assertRaises(NotUndirectedGraph):
            list(mst_prim(self.digraph, 1))

    def test_mst_prim_missing_node(self):
        with self.assertRaises(NodeNotFound):
            list(mst_prim(self.graph, 999))