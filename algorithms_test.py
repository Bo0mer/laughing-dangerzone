import unittest

from algorithms import *


class AlgorithmsTest(unittest.TestCase):

	def test_dfs(self):
		g = Graph()
		g.add_edge(1, 2)
		g.add_edge(2, 3)
		g.add_edge(3, 5)
		g.add_edge(2, 7)
		g.add_edge(7, 'Sofia')
		g.add_edge('Bourgas', 'Varna')

		self.assertEqual(list(dfs(g, 1)), 
			[(1, 2), (2, 3), (2, 7), (7, 'Sofia'), (3, 5)])

		self.assertEqual(list(dfs(g, 'Bourgas')), [('Bourgas', 'Varna')])

	def test_bfs(self):
		g = Graph()
		g.add_edge(1, 2)
		g.add_edge(1, 3)
		g.add_edge(2, 4)
		g.add_edge(4, 'Sofia')
		g.add_edge(4, 'Bourgas')
		g.add_edge(4, 'London')
		must_be = {0: {1: {2, 3}},
					1: {2: {4}, 3: set()},
					2: {4: {'London', 'Sofia', 'Bourgas'}},
					3: {'London': set(), 'Sofia': set(), 'Bourgas': set()}}

		for level, graph_level in enumerate(bfs(g, 1)):
			self.assertEqual(must_be[level], graph_level)

	def test_connected_components(self):
		g = Graph()
		g.add_edge(1, 2)
		self.assertEqual(connected_components(g), 1)
		g.add_edge(3, 2)
		self.assertEqual(connected_components(g), 1)
		g.add_edge('Sofia', 'Varna')
		self.assertEqual(connected_components(g), 2)
		g.add_edge('Varna', 1)
		self.assertEqual(connected_components(g), 1)
		g.add_node('LeftAlone')
		self.assertEqual(connected_components(g), 2)
		g.add_node('AlsoLeftAlone')
		self.assertEqual(connected_components(g), 3)
		g.add_edge('LeftAlone', 'AlsoLeftAlone')
		self.assertEqual(connected_components(g), 2)

	def test_unweighted_shortest_path(self):
		g = Graph()
		g.add_edge(1, 2)
		g.add_edge(2, 3)
		g.add_edge(3, 4)
		g.add_edge(4, 5)
		g.add_edge(1, 'Sofia')
		g.add_edge('Sofia', 5)
		self.assertEqual(unweighted_shortest_path(g, 1, 5), [1, 'Sofia', 5])

	def test_unweighted_shortest_path_without_path(self):
		g = Graph()
		g.add_edge(1, 2)
		g.add_edge(2, 3)
		g.add_edge(3, 4)
		g.add_edge(1, 'Sofia')
		g.add_node(5)
		self.assertEqual(unweighted_shortest_path(g, 1, 5), None)

if __name__ == '__main__':
	unittest.main()