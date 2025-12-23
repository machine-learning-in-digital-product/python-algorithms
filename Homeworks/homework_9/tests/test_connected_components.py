import unittest

from src.connected_components import connected_components


class ConnectedComponentsTests(unittest.TestCase):
    def test_empty_graph(self) -> None:
        self.assertEqual(connected_components({}), [])

    def test_isolated_vertices(self) -> None:
        graph = {"a": [], "b": [], "c": []}
        comps = connected_components(graph)
        self.assertEqual(sorted(comps), [["a"], ["b"], ["c"]])

    def test_single_component(self) -> None:
        graph = {"a": ["b"], "b": ["a", "c"], "c": ["b"]}
        self.assertEqual(connected_components(graph), [["a", "b", "c"]])

    def test_two_components(self) -> None:
        graph = {"a": ["b"], "b": ["a"], "c": [], "d": ["e"], "e": ["d"]}
        comps = connected_components(graph)
        self.assertEqual(sorted(comps), [["a", "b"], ["c"], ["d", "e"]])

    def test_asymmetric_edges_still_connected(self) -> None:
        graph = {"a": ["b"], "b": [], "c": ["d"], "d": []}
        comps = connected_components(graph)
        self.assertEqual(sorted(comps), [["a", "b"], ["c", "d"]])


if __name__ == "__main__":
    unittest.main()

