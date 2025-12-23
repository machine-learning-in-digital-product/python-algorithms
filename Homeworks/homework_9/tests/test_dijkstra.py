import unittest

from src.dijkstra import dijkstra


class DijkstraTests(unittest.TestCase):
    def test_basic(self) -> None:
        graph = {
            "s": [("a", 1), ("b", 4)],
            "a": [("b", 2), ("c", 5)],
            "b": [("c", 1)],
            "c": [],
        }
        dist, parent = dijkstra(graph, "s")
        self.assertEqual(dist["c"], 4)  # s -> a -> b -> c
        self.assertEqual(parent["c"], "b")
        self.assertEqual(parent["b"], "a")
        self.assertEqual(parent["a"], "s")

    def test_unreachable_node(self) -> None:
        graph = {"s": [("a", 1)], "a": [], "b": []}
        dist, parent = dijkstra(graph, "s")
        self.assertEqual(dist["b"], float("inf"))
        self.assertIsNone(parent["b"])

    def test_zero_weight_edges(self) -> None:
        graph = {"s": [("a", 0)], "a": [("b", 0)], "b": []}
        dist, _ = dijkstra(graph, "s")
        self.assertEqual(dist["b"], 0)

    def test_negative_weight_raises(self) -> None:
        graph = {"s": [("a", -1)], "a": []}
        with self.assertRaises(ValueError):
            dijkstra(graph, "s")

    def test_missing_source_raises(self) -> None:
        graph = {"a": []}
        with self.assertRaises(ValueError):
            dijkstra(graph, "s")


if __name__ == "__main__":
    unittest.main()

