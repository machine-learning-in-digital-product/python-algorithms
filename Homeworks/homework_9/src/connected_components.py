from __future__ import annotations

from typing import Any, Iterable, List, Set, Dict


def connected_components(graph: Dict[Any, Iterable[Any]]) -> List[List[Any]]:
    visited: Set[Any] = set()
    components: List[List[Any]] = []

    for start in sorted(graph.keys(), key=repr):
        if start in visited:
            continue
        stack = [start]
        comp: List[Any] = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            comp.append(node)
            for neigh in sorted(graph.get(node, ()), key=repr, reverse=True):
                if neigh not in visited:
                    stack.append(neigh)
        components.append(sorted(comp, key=repr))

    return components

