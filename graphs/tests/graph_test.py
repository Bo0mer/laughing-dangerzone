import unittest

from graphs.graphs import Graph


class BasicGraphTest(unittest.TestCase):

    def setUp(self):
        self.nodes = [1, 'Sofia', 'Bourgas', 5.6555]
        self.edges = [(1, 'Sofia'), ('Sofia', 'Bourgas')]
        self.graph = Graph()
        for node in self.nodes:
            self.graph.add_node(node)

        for edge in self.edges:
            self.graph.add_edge(*edge)

    def tearDown(self):
        del self.nodes
        del self.graph

    def test_nodes_in_graph(self):
        for node in self.nodes:
            self.assertTrue(node in self.graph)
        self.assertFalse('NotANode' in self.graph)

    def test_edges_in_graph(self):
        for edge in self.edges:
            self.assertTrue(edge[0] in self.graph[edge[1]])
            self.assertTrue(edge[1] in self.graph[edge[0]])
        not_an_edge = 1, 'Bourgas'
        self.assertFalse(not_an_edge[0] in self.graph[not_an_edge[1]])
        self.assertFalse(not_an_edge[1] in self.graph[not_an_edge[0]])

    def test_has_edge(self):
        for edge in self.edges:
            self.assertTrue(self.graph.has_edge(*edge))
        not_an_edge = 1, 'Bourgas'
        self.assertFalse(self.graph.has_edge(*not_an_edge))

    def test_remove_edge(self):
        edge = 1, 'Bourgas'
        self.graph.add_edge(*edge)
        self.graph.remove_edge(*edge)
        self.assertFalse(self.graph.has_edge(*edge))

    def test_size(self):
        self.assertEqual(self.graph.size(), len(self.edges))

    def test_order(self):
        self.assertEqual(self.graph.order(), len(self.nodes))

    def test_degree(self):
        for node in self.nodes:
            self.assertEqual(self.graph.degree(node),
                            sum([edge.count(node) for edge in self.edges]))

    def test_is_directed(self):
        self.assertFalse(self.graph.is_directed())


if __name__ == '__main__':
    unittest.main()