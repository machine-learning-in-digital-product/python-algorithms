import random
import pytest
from src.two_sum import two_sum_indices

@pytest.mark.parametrize(
    "arr,k,expected",
    [
        # базовые
        ([2, 7, 11, 15], 9, (0, 1)),
        ([1, 2, 3, 4, 5], 9, (3, 4)),
        ([5, 4, 3, 2, 1], 3, (3, 4)),  # 2 + 1
        # с отрицательными
        ([-3, 4, 3, 90], 0, (0, 2))
    ],
)
def test_known_cases(arr, k, expected):
    i, j = two_sum_indices(arr, k)
    assert arr[i] + arr[j] == k
    assert (i, j) == expected

def test_duplicates_single_solution():
    # Дубликаты допустимы, пара ровно одна
    arr = [3, 3, 4, 6]
    k = 6
    i, j = two_sum_indices(arr, k)
    assert arr[i] + arr[j] == k
    assert (i, j) == (0, 1)  # первая подходящая пара (3 + 3)

def test_order_sorted_indices():
    arr = [10, -1, 5]
    k = 9  # 10 + (-1) = 9
    i, j = two_sum_indices(arr, k)
    assert i < j

def test_raises_when_no_pair_optional():
    from src.two_sum import two_sum_indices
    with pytest.raises(ValueError):
        two_sum_indices([1, 2, 3], 100)
