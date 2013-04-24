import unittest

from graphs.digraphs import DiGraph


class BasicDiGraphTest(unittest.TestCase):

    def setUp(self):
        self.nodes = [1, 'Sofia', 'Bourgas', 5.6555]
        self.edges = [(1, 'Sofia'), ('Sofia', 'Bourgas')]
        self.graph = DiGraph()
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

    def test_edges_successors_predecessors(self):
        for (u, v) in self.edges:
            self.assertTrue(u in self.graph.get_predecessors(v))
            self.assertTrue(v in self.graph.get_successors(u))
            self.assertFalse(v in self.graph.get_predecessors(u))
            self.assertFalse(u in self.graph.get_successors(v))

    def test_has_edge(self):
        for (u, v) in self.edges:
            self.assertTrue(self.graph.has_edge(u, v))

    def test_remove_edge(self):
        u, v = 1, 'Bourgas'
        self.assertFalse(self.graph.has_edge(u, v))
        self.graph.add_edge(u, v)
        self.assertTrue(self.graph.has_edge(u, v))
        self.graph.remove_edge(u, v)
        self.assertFalse(self.graph.has_edge(u, v))

    def test_is_directed(self):
        self.assertTrue(self.graph.is_directed())

    def test_in_degree(self):
        self.assertEqual(self.graph.in_degree('Sofia'), 1)
        self.assertEqual(self.graph.in_degree(1), 0)

    def test_out_degree(self):
        self.assertEqual(self.graph.out_degree('Sofia'), 1)
        self.assertEqual(self.graph.out_degree('Bourgas'), 0)

    def test_degree(self):
        self.assertEqual(self.graph.degree('Sofia'), 2)
        self.assertEqual(self.graph.degree(5.6555), 0)

    def test_order(self):
        self.assertEqual(self.graph.order(), len(self.nodes))
        self.graph.add_node('AloneNode')
        self.assertEqual(self.graph.order(), len(self.nodes)+1)
        self.graph.remove_node('AloneNode')
        self.assertEqual(self.graph.order(), len(self.nodes))

    def test_size(self):
        self.assertEqual(self.graph.size(), len(self.edges))
        self.graph.add_edge(100, 100)
        self.assertEqual(self.graph.size(), len(self.edges) + 1)
        self.graph.remove_node(100)
        self.assertEqual(self.graph.size(), len(self.edges))

if __name__ == '__main__':
    unittest.main()