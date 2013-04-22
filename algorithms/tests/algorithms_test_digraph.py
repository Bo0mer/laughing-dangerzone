import unittest

from graphs.digraphs import DiGraph
from algorithms.traversal import *
from algorithms.connectivity import *
from algorithms.shortest_paths import *
from algorithms.mst import *

class DiAlgorithmsTest(unittest.TestCase):

	def  test_dfs(self):
		g = DiGraph()
		g.add_edge(1, 2)
		g.add_edge(2, 3)
		g.add_edge(4, 1)

		self.assertEqual(list(dfs(g, 1)),
						[(1, 2), (2, 3)])

	def test_bfs(self):
		g = DiGraph()
		g.add_edge(1, 2)
		g.add_edge(2, 3)
		g.add_edge(2, 4)
		g.add_edge(7, 1)
		g.add_edge(6, 1)
		self.assertEqual(list(bfs(g, 1)),
						[{1: {2}},
						{2: {3, 4}},
						{3: set(), 4: set()}])

	def test_unweighted_shortest_path(self):
		g = DiGraph()
		g.add_edge(1, 2)
		g.add_edge(2, 6)
		g.add_edge(6, 12)
		g.add_edge(12, 1)
		g.add_edge(1, 4)
		g.add_edge(4, 8)
		g.add_edge(8, 666)
		g.add_edge(666, 12)
		self.assertEqual(unweighted_shortest_path(g, 1, 12),
						[1, 2, 6, 12])

	def test_unweighted_shortest_path_without_path(self):
		g = DiGraph()
		g.add_edge(1, 3)
		g.add_edge(3, 5)
		g.add_edge(5, 12)
		g.add_edge(1, 7)
		g.add_edge(7, 12)
		g.add_edge(1, 12)
		self.assertEqual(unweighted_shortest_path(g, 12, 1),
						None)

	def test_shortest_paths_from(self):
		g = DiGraph()
		g.add_edge('London', 'Sofia', weight=2500)
		g.add_edge('London', 'New York', weight=7500)
		g.add_edge('Sofia', 'Chicago', weight=9000)
		g.add_edge('Chicago', 'New York', weight=975)
		g.add_edge('Lisbon', 'Sidney', weight=12000)

		self.assertEqual(shortest_paths_from(g, 'Sofia'),
					{'New York': 9975, 'Chicago': 9000, 'Sofia': 0})

	def test_shortest_patsh_from_with_negative_edge(self):
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
						{1: 0, 2: 7, 3: -2, 4: 2, 5: 4})

	def test_shortest_paths_from_without_path(self):
		g = DiGraph()
		g.add_edge('London', 'Chicago', weight=7600)
		g.add_edge('Chicago', 'New York', weight=975)
		g.add_edge('Sofia', 'Lisbon', weight=10000)
		g.add_node('Pernik')
		self.assertEqual(shortest_paths_from(g, 'Pernik'),
					{'Pernik': 0})

	def test_dijkstra(self):
		g = DiGraph()
		g.add_edge('A', 'B', w=10)
		g.add_edge('A', 'C', w=19)
		g.add_edge('B', 'C', w=2)
		g.add_edge('C', 'B', w=4)
		g.add_edge('B', 'D', w=1)
		g.add_edge('C', 'D', w=8)
		g.add_edge('C', 'E', w=5)
		g.add_edge('D', 'E', w=7)
		g.add_edge('E', 'D', w=4)
		self.assertEqual(dijkstra(g, 'A', weight_attribute='w'),
				{'E': 17, 'D': 11, 'A': 0, 'C': 12, 'B': 10})

	def test_dijkstra_with_no_path(self):
		g = DiGraph()
		g.add_edge(2, 3, weight=10)
		g.add_edge(3, 5, weight=5)
		g.add_edge(2, 5, weight=17)
		g.add_node(1)
		self.assertEqual(dijkstra(g, 1), {1: 0})

if __name__ == '__main__':
	unittest.main()