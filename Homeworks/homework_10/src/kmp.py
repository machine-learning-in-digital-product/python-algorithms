from typing import List


def _build_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    if pattern == "":
        raise ValueError("Pattern must not be empty")
    n, m = len(text), len(pattern)
    if m > n:
        return []
    lps = _build_lps(pattern)
    result: List[int] = []
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - m)
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
    return result

