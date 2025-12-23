from typing import List


def rabin_karp_search(text: str, pattern: str, base: int = 256, mod: int = 1_000_000_007) -> List[int]:
    if pattern == "":
        raise ValueError("Pattern must not be empty")
    n, m = len(text), len(pattern)
    if m > n:
        return []
    pattern_hash = 0
    window_hash = 0
    base_power = pow(base, m - 1, mod)
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    result: List[int] = []
    for i in range(n - m + 1):
        if pattern_hash == window_hash and text[i : i + m] == pattern:
            result.append(i)
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * base_power) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash %= mod
    return result

