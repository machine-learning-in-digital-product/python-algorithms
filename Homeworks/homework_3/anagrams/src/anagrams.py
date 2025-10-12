from collections import defaultdict
from typing import List

def group_anagrams(strs):
    groups: dict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
