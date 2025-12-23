from __future__ import annotations

import heapq
from typing import Any, Dict, Iterable, List, Optional, Tuple


def dijkstra(
    graph: Dict[Any, Iterable[Tuple[Any, float]]],
    source: Any,
) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
    if source not in graph:
        raise ValueError("Source node is not in the graph")

    for _, edges in graph.items():
        for _, w in edges:
            if w < 0:
                raise ValueError("Negative edge weight detected; Dijkstra requires non-negative weights")

    distances: Dict[Any, float] = {node: float("inf") for node in graph}
    parents: Dict[Any, Optional[Any]] = {node: None for node in graph}
    distances[source] = 0.0

    heap: List[Tuple[float, Any]] = [(0.0, source)]
    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u != distances[u]:
            continue
        for v, w in graph.get(u, ()):
            new_dist = dist_u + w
            if new_dist < distances.get(v, float("inf")):
                distances[v] = new_dist
                parents[v] = u
                heapq.heappush(heap, (new_dist, v))
                if v not in parents:
                    parents[v] = u
            elif v not in parents:
                parents[v] = None
                distances[v] = float("inf")
    return distances, parents

