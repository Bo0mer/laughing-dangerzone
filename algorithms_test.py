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

if __name__ == '__main__':
	unittest.main()