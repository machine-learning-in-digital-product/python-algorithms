import pytest
from src.prime_number import count_primes_below

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 0),
    (2, 0),      # простых < 2 нет
    (3, 1),      # {2}
    (10, 4),     # {2,3,5,7}
    (20, 8),     # {2,3,5,7,11,13,17,19}
    (100, 25),
    (1000, 168),
])
def test_known_counts(n, expected):
    assert count_primes_below(n) == expected

def test_monotonicity_small_range():
    # количество простых не убывает при увеличении n
    prev = 0
    for n in range(2, 200):
        cur = count_primes_below(n)
        assert cur >= prev
        prev = cur

def test_against_naive_for_small_n():
    # сравнение с наивной проверкой для небольших n
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        d = 2
        while d * d <= k:
            if k % d == 0:
                return False
            d += 1
        return True

    for n in range(2, 300):
        expected = sum(1 for x in range(n) if is_prime(x))
        assert count_primes_below(n) == expected
        