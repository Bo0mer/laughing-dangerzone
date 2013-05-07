import unittest

from graphs.digraphs import DiGraph
from algorithms.traversal import *
from algorithms.connectivity import *
from algorithms.shortest_paths import *
from algorithms.mst import *
from algorithms.max_path import *
from algorithms.eulerian import *


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

    def test_unweighted_shortest_paths(self):
        g = DiGraph()
        g.add_edge(1, 2)
        g.add_edge(2, 6)
        g.add_edge(6, 12)
        g.add_edge(12, 1)
        g.add_edge(1, 4)
        g.add_edge(4, 8)
        g.add_edge(8, 666)
        g.add_edge(666, 12)
        self.assertEqual(unweighted_shortest_paths(g, 1),
                        ({1: None, 2: 1, 4: 1, 6: 2,
                         8: 4, 666: 8, 12: 6},
                         {1: 0, 2: 1, 4: 1, 6: 2,
                          8: 2, 666: 3, 12: 3}))

    def test_shortest_paths_from(self):
        g = DiGraph()
        g.add_edge('London', 'Sofia', weight=2500)
        g.add_edge('London', 'New York', weight=7500)
        g.add_edge('Sofia', 'Chicago', weight=9000)
        g.add_edge('Chicago', 'New York', weight=975)
        g.add_edge('Lisbon', 'Sidney', weight=12000)

        self.assertEqual(shortest_paths_from(g, 'Sofia'),
                    ({'Sofia': None, 'Chicago': 'Sofia', 'New York': 'Chicago'},
                    {'New York': 9975, 'Chicago': 9000, 'Sofia': 0}))

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
                        ({1: None, 2: 1, 3: 4, 4: 5, 5: 2},
                        {1: 0, 2: 7, 3: -2, 4: 2, 5: 4}))

    def test_shortest_paths_from_without_path(self):
        g = DiGraph()
        g.add_edge('London', 'Chicago', weight=7600)
        g.add_edge('Chicago', 'New York', weight=975)
        g.add_edge('Sofia', 'Lisbon', weight=10000)
        g.add_node('Pernik')
        self.assertEqual(shortest_paths_from(g, 'Pernik'),
                     ({'Pernik': None}, {'Pernik': 0}))

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
            ({'A': None, 'B': 'A', 'C': 'B', 'D': 'B', 'E': 'C'},
             {'E': 17, 'D': 11, 'A': 0, 'C': 12, 'B': 10}))

    def test_dijkstra_with_no_path(self):
        g = DiGraph()
        g.add_edge(2, 3, weight=10)
        g.add_edge(3, 5, weight=5)
        g.add_edge(2, 5, weight=17)
        g.add_node(1)
        self.assertEqual(dijkstra(g, 1), ({1: None}, {1: 0}))

    def test_strongly_connected_components(self):
        g = DiGraph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        g.add_edge(7, 6)
        sccs = [{1, 2, 3}, {4, 5}, {6, 7}]
        sccs_result = strongly_connected_components(g)
        self.assertEqual(len(sccs), len(sccs_result))
        for scc in sccs:
            self.assertTrue(scc in sccs_result)

    def test_max_path(self):
        g = DiGraph()
        g.add_edge(1, 3, w=3)
        g.add_edge(2, 3, w=5)
        g.add_edge(3, 5, w=11)
        g.add_edge(3, 4, w=8)
        g.add_edge(5, 6, w=12)
        g.add_edge(4, 7, w=16)
        g.add_edge(5, 7, w=14)
        g.add_edge(4, 6, w=18)
        g.add_edge(6, 8, w=21)
        g.add_edge(4, 7, w=16)
        g.add_edge(7, 8, w=16)
        g.add_edge(8, 10, w=7)
        g.add_edge(8, 9, w=5)
        pred, distance = max_path(g, weight_attribute='w')
        self.assertEqual(59, max(distance.values()))
        self.assertEqual(pred,
                        {3: 2, 4: 3, 5: 3, 6: 4,
                         7: 5, 8: 6, 9: 8, 10: 8})

    def test_is_eulerian(self):
        g = DiGraph()
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