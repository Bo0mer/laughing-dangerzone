import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.traversal import bfs, dfs
from exceptions.algoexceptions import NodeNotFound


class TraversalTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        g = self.graph
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 5)
        g.add_edge(2, 7)
        g.add_edge(7, 'Sofia')
        g.add_edge('Bourgas', 'Varna')

        self.digraph = DiGraph()
        dig = self.digraph
        dig.add_edge(1, 2)
        dig.add_edge(2, 3)
        dig.add_edge(2, 4)
        dig.add_edge(7, 1)
        dig.add_edge(6, 1)

    def tearDown(self):
        del self.graph
        del self.digraph

    def test_dfs_with_graph(self):
        self.assertEqual(list(dfs(self.graph, 1)),
                         [(1, 2), (2, 3), (2, 7), (7, 'Sofia'), (3, 5)])

    def test_dfs_with_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            list(dfs(self.graph, 999))

    def test_dfs_with_digraph(self):
        self.assertEqual(list(dfs(self.digraph, 1)),
                         [(1, 2), (2, 3), (2, 4)])

    def test_dfs_with_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            list(dfs(self.digraph, 'NotANode'))

    def test_bfs_with_graph(self):
        self.assertEqual(list(bfs(self.graph, 1)),
                         [{1: {2}}, {2: {3, 7}},
                         {3: {5}, 7: {'Sofia'}},
                         {'Sofia': set(), 5: set()}])

    def test_bfs_with_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            list(bfs(self.graph, 999))

    def test_bfs_with_digraph(self):
        self.assertEqual(list(bfs(self.digraph, 1)),
                         [{1: {2}}, {2: {3, 4}}, {3: set(), 4: set()}])

    def test_bfs_with_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            list(bfs(self.digraph, 999))
