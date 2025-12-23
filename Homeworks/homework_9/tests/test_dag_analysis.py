import unittest

from src.dag_analysis import analyze_dag


class DagAnalysisTests(unittest.TestCase):
    def test_cycle_detection(self) -> None:
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        has_cycle, cycle, topo = analyze_dag(graph)
        self.assertTrue(has_cycle)
        self.assertIsNotNone(cycle)
        self.assertIsNone(topo)
        # cycle should start and end at same node
        self.assertEqual(cycle[0], cycle[-1])

    def test_cycle_single_self_loop(self) -> None:
        graph = {"a": ["a"], "b": []}
        has_cycle, cycle, topo = analyze_dag(graph)
        self.assertTrue(has_cycle)
        self.assertIsNone(topo)
        self.assertEqual(cycle[0], "a")
        self.assertEqual(cycle[-1], "a")

    def test_acyclic_topo(self) -> None:
        graph = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
        has_cycle, cycle, topo = analyze_dag(graph)
        self.assertFalse(has_cycle)
        self.assertIsNone(cycle)
        self.assertEqual(set(topo), {"a", "b", "c", "d"})
        # 'a' must precede both 'b' and 'c'; 'b' and 'c' precede 'd'
        self.assertLess(topo.index("a"), topo.index("b"))
        self.assertLess(topo.index("a"), topo.index("c"))
        self.assertLess(topo.index("b"), topo.index("d"))
        self.assertLess(topo.index("c"), topo.index("d"))

    def test_empty_graph(self) -> None:
        has_cycle, cycle, topo = analyze_dag({})
        self.assertFalse(has_cycle)
        self.assertIsNone(cycle)
        self.assertEqual(topo, [])


if __name__ == "__main__":
    unittest.main()

