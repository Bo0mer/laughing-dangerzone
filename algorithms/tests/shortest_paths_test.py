import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from algorithms.shortest_paths import *
from exceptions.algoexceptions import NodeNotFound, NegativeCycle


class ShortestPathsTest(unittest.TestCase):
    def setUp(self):
        self.positive_graph = Graph()
        pg = self.positive_graph
        pg.add_edge(1, 2, w=5)
        pg.add_edge(1, 3, w=29)
        pg.add_edge(1, 6, w=70)
        pg.add_edge(2, 3, w=10)
        pg.add_edge(2, 4, w=15)
        pg.add_edge(3, 4, w=51)
        pg.add_edge(4, 5, w=6)
        pg.add_edge(3, 6, w=10)

        self.positive_digraph = DiGraph()
        pdig = self.positive_digraph
        pdig.add_edge(1, 2, w=5)
        pdig.add_edge(1, 3, w=29)
        pdig.add_edge(1, 6, w=70)
        pdig.add_edge(2, 3, w=10)
        pdig.add_edge(2, 4, w=15)
        pdig.add_edge(3, 4, w=51)
        pdig.add_edge(4, 5, w=6)
        pdig.add_edge(3, 6, w=10)

    def tearDown(self):
        del self.positive_digraph
        del self.positive_graph

    def test_unweighted_shortest_paths_graph(self):
        self.assertEqual(
            unweighted_shortest_paths(self.positive_graph, 1, 2),
            ({1: None, 2: 1, 3: 1, 4: 3, 5: 4, 6: 1},
             {1: 0, 2: 2, 3: 2, 4: 4, 5: 6, 6: 2}))

    def test_unweighted_shortest_paths_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            unweighted_shortest_paths(self.positive_graph, 999)

    def test_unweighted_shortest_paths_digraph(self):
        self.assertEqual(
            unweighted_shortest_paths(self.positive_digraph, 1),
            ({1: None, 2: 1, 3: 1, 4: 3, 5: 4, 6: 1},
             {1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 1}))

    def test_unweighted_shortest_paths_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            unweighted_shortest_paths(self.positive_digraph, 999)

    def test_bellman_ford_graph(self):
        self.assertEqual(
            shortest_paths_from(self.positive_graph, 1, weight_attribute='w'),
            ({1: None, 2: 1, 3: 2, 4: 2, 5: 4, 6: 3},
             {1: 0, 2: 5, 3: 15, 4: 20, 5: 26, 6: 25}))

    def test_bellman_ford_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            shortest_paths_from(self.positive_graph, 999)

    def test_bellman_ford_graph_negative_edges(self):
        self.positive_graph.add_edge(1, 100, w=-1)
        with self.assertRaises(NegativeCycle):
            shortest_paths_from(self.positive_graph, 1, weight_attribute='w')
        self.positive_graph.remove_edge(1, 100)

    def test_bellman_ford_digraph(self):
        self.assertEqual(
            shortest_paths_from(
                self.positive_digraph, 1, weight_attribute='w'),
            ({1: None, 2: 1, 3: 2, 4: 2, 5: 4, 6: 3},
             {1: 0, 2: 5, 3: 15, 4: 20, 5: 26, 6: 25}))

    def test_bellman_ford_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            shortest_paths_from(self.positive_digraph, 999)

    def test_bellman_ford_digraph_negative_edges(self):
        g = DiGraph()
        g.add_edge(1, 2, w=7)
        g.add_edge(1, 4, w=6)
        g.add_edge(4, 5, w=5)
        g.add_edge(5, 4, w=-2)
        g.add_edge(2, 3, w=9)
        g.add_edge(2, 5, w=-3)
        g.add_edge(4, 2, w=8)
        g.add_edge(4, 3, w=-4)
        g.add_edge(3, 1, w=7)
        g.add_edge(3, 5, w=7)
        self.assertEqual(shortest_paths_from(g, 1, weight_attribute='w'),
                         ({1: None, 2: 1, 3: 4, 4: 5, 5: 2},
                          {1: 0, 2: 7, 3: -2, 4: 2, 5: 4}))

    def test_bellman_ford_digraph_negative_cycle(self):
        self.positive_digraph.add_edge(2, 1, w=-6)
        with self.assertRaises(NegativeCycle):
            shortest_paths_from(
                self.positive_digraph, 1, weight_attribute='w')
        self.positive_digraph.remove_edge(2, 1)

    def test_dijkstra_graph(self):
        self.assertEqual(
            dijkstra(self.positive_graph, 1, weight_attribute='w'),
            ({1: None, 2: 1, 3: 2, 4: 2, 5: 4, 6: 3},
             {1: 0, 2: 5, 3: 15, 4: 20, 5: 26, 6: 25}))

    def test_dijkstra_graph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            dijkstra(self.positive_graph, 999)

    def test_dijkstra_digraph(self):
        self.assertEqual(
            dijkstra(self.positive_digraph, 1, weight_attribute='w'),
            ({1: None, 2: 1, 3: 2, 4: 2, 5: 4, 6: 3},
             {1: 0, 2: 5, 3: 15, 4: 20, 5: 26, 6: 25}))

    def test_dijkstra_digraph_missing_node(self):
        with self.assertRaises(NodeNotFound):
            dijkstra(self.positive_digraph, 999)
