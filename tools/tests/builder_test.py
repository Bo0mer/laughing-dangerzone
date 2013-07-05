import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from tools.builder import *
from exceptions.algoexceptions import InvalidDegreeSequence


class BuilderTest(unittest.TestCase):
    def setUp(self):
        self.valid_degree_sequence = [3, 3, 3, 3, 3, 3, 4, 4, 4]
        self.valid_didegree_sequence = [(2, 1), (1, 1), (1, 1), (0, 1)]

    def tearDown(self):
        del self.valid_degree_sequence
        del self.valid_didegree_sequence

    def test_is_valid_degree_sequence(self):
        self.assertTrue(
            is_valid_degree_sequence(self.valid_degree_sequence))

    def test_is_valid_degree_sequence_invalid(self):
        self.assertFalse(
            is_valid_degree_sequence([1, 1, 1, 2]))

        self.assertFalse(
            is_valid_degree_sequence([2, 1, -1]))

        self.assertFalse(
            is_valid_degree_sequence([6, 1, 1, 2]))

    def test_build_graph(self):
        nodes = {'node' + str(k): self.valid_degree_sequence[k]
                 for k in range(9)}
        graph = build_graph(self.valid_degree_sequence, sorted(nodes))

        for node in graph:
            self.assertEqual(graph.degree(node), nodes[node])

    def test_build_graph_fail(self):
        with self.assertRaises(InvalidDegreeSequence):
            build_graph([-3, 100, 566])

    def test_build_graph_only_nodes(self):
        graph = build_graph([0, 0, 0, 0], ['a', 'b', 'c', 'd'])
        self.assertEqual(graph.size(), 0)
        self.assertEqual(graph.order(), 4)

    def test_is_valid_didegree_sequence(self):
        self.assertTrue(
            is_valid_directed_degree_sequence(self.valid_didegree_sequence))

    def test_is_valid_didegree_sequence_invalid(self):
        invalid = [(3, 1), (-5, 2), (0, 1)]
        self.assertFalse(
            is_valid_directed_degree_sequence(invalid))

    def test_build_digraph(self):
        nodes = {'node' + str(k): self.valid_didegree_sequence[k]
                 for k in range(4)}
        graph = build_digraph(self.valid_didegree_sequence, sorted(nodes))

        for node in graph:
            self.assertEqual(
                (graph.out_degree(node), graph.in_degree(node)), nodes[node])

    def test_build_digraph_fail(self):
        with self.assertRaises(InvalidDegreeSequence):
            build_digraph([(3, 1), (-5, 2), (0, 1)])

    def test_build_digraph_only_nodes(self):
        digraph = build_digraph([(0, 0), (0, 0)])
        self.assertEqual(digraph.size(), 0)
        self.assertEqual(digraph.order(), 2)
