import unittest

from graphs.graphs import Graph
from algorithms.traversal import *
from algorithms.connectivity import *
from algorithms.shortest_paths import *
from algorithms.mst import *
from algorithms.eulerian import *


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
        self.assertEqual(number_connected_components(g), 1)
        g.add_edge(3, 2)
        self.assertEqual(number_connected_components(g), 1)
        g.add_edge('Sofia', 'Varna')
        self.assertEqual(number_connected_components(g), 2)
        g.add_edge('Varna', 1)
        self.assertEqual(number_connected_components(g), 1)
        g.add_node('LeftAlone')
        self.assertEqual(number_connected_components(g), 2)
        g.add_node('AlsoLeftAlone')
        self.assertEqual(number_connected_components(g), 3)
        g.add_edge('LeftAlone', 'AlsoLeftAlone')
        self.assertEqual(number_connected_components(g), 2)

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

    def test_shortest_paths_from(self):
        g = Graph()
        g.add_edge('London', 'Sofia', weight=2500)
        g.add_edge('London', 'New York', weight=7500)
        g.add_edge('Sofia', 'Chicago', weight=9000)
        g.add_edge('Chicago', 'New York', weight=975)
        g.add_edge('Lisbon', 'Sidney', weight=12000)

        self.assertEqual(shortest_paths_from(g, 'Sofia'),
                    {'London': 2500, 'New York': 9975,
                     'Chicago': 9000, 'Sofia': 0})

    def test_shortest_paths_from_without_path(self):
        g = Graph()
        g.add_edge('London', 'Chicago', weight=7600)
        g.add_edge('Chicago', 'New York', weight=975)
        g.add_edge('Sofia', 'Lisbon', weight=10000)
        g.add_node('Pernik')
        self.assertEqual(shortest_paths_from(g, 'Pernik'),
                    {'Pernik': 0})

    def test_dijkstra(self):
        g = Graph()
        g.add_edge(1, 2, weight=5)
        g.add_edge(1, 3, weight=29)
        g.add_edge(1, 6, weight=70)
        g.add_edge(2, 3, weight=10)
        g.add_edge(2, 4, weight=15)
        g.add_edge(3, 4, weight=51)
        g.add_edge(4, 5, weight=6)
        g.add_edge(3, 6, weight=10)
        self.assertEqual(dijkstra(g, 1),
                        {1: 0, 2: 5, 3: 15,
                         4: 20, 5: 26, 6: 25})

    def test_dijkstra_with_no_path(self):
        g = Graph()
        g.add_edge(2, 3, weight=10)
        g.add_edge(3, 5, weight=5)
        g.add_edge(2, 5, weight=17)
        g.add_node(1)
        self.assertEqual(dijkstra(g, 1), {1: 0})


    def test_mst_prim_sum(self):
        g = Graph()
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
        for i in range(1, 9):
            self.assertEqual(sum([weight for u, v, weight in mst_prim(g, i)]),
                        53)

    def test_mst_prim_tree(self):
        g = Graph()
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
        self.assertEqual(list(mst_prim(g, 1)),
                        [(1, 2, 3), (2, 8, 8), (8, 6, 5),
                         (8, 7, 6), (6, 3, 7), (6, 5, 9), 
                         (3, 4, 15)])

    def test_is_eulerian(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 1)
        self.assertTrue(is_eulerian(g))
        g.add_edge(6, 7)
        self.assertFalse(is_eulerian(g))
        g.remove_edge(6, 7)
        g.add_edge(1, 3)
        self.assertFalse(is_eulerian(g))


if __name__ == '__main__':
    unittest.main()