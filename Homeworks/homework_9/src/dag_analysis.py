from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Tuple


def analyze_dag(graph: Dict[Any, Iterable[Any]]) -> Tuple[bool, Optional[List[Any]], Optional[List[Any]]]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color: Dict[Any, int] = {node: WHITE for node in graph}
    parent: Dict[Any, Any] = {}
    cycle: Optional[List[Any]] = None
    topo: List[Any] = []

    def dfs(node: Any) -> bool:
        nonlocal cycle
        color[node] = GRAY
        for neigh in graph.get(node, ()):
            if color.get(neigh, WHITE) == WHITE:
                parent[neigh] = node
                if dfs(neigh):
                    return True
            elif color.get(neigh) == GRAY:
                cycle = build_cycle(node, neigh, parent)
                return True
        color[node] = BLACK
        topo.append(node)
        return False

    def build_cycle(cur: Any, target: Any, parent_map: Dict[Any, Any]) -> List[Any]:
        path = [target, cur]
        while cur != target:
            cur = parent_map[cur]
            path.append(cur)
        path.reverse()
        path.append(path[0])
        return path

    for node in sorted(graph.keys(), key=repr):
        if color[node] == WHITE:
            if dfs(node):
                return True, cycle, None

    topo.reverse()
    return False, None, topo

