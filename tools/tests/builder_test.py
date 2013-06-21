import unittest

from graphs.graphs import Graph
from graphs.digraphs import DiGraph
from tools.builder import *
from exceptions.algoexceptions import InvalidDegreeSequence


class BuilderTest(unittest.TestCase):
    def setUp(self):
        self.valid_degree_sequence = [3, 3, 3, 3, 3, 3, 4, 4, 4]
    
    def tearDown(self):
        del self.valid_degree_sequence

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
        nodes = {'node' + str(k): self.valid_degree_sequence[k] for k in range(9)}
        graph = build_graph(self.valid_degree_sequence, sorted(nodes))

        for node in graph:
            self.assertEqual(graph.degree(node), nodes[node])

    def test_build_graph_fail(self):
        with self.assertRaises(InvalidDegreeSequence):
            build_graph([-3, 100, 566])
