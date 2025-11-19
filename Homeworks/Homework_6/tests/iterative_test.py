import random
import sys
import time
import functools

from Iterative import mergesort_iterative, quicksort_iterative


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


@measure_time
def mergesort_iter_timed(arr):
    return mergesort_iterative(arr)

@measure_time
def quicksort_iter_timed(arr):
    return quicksort_iterative(arr)


if __name__ == "__main__":
    sys.setrecursionlimit(50_000)

    n = 20_000

    random_list = [random.randint(0, 1_000_000) for _ in range(n)]
    sorted_list = list(range(n))
    reversed_list = list(range(n, 0, -1))

    print("=== Случайные данные ===")
    ms_it_rand = mergesort_iter_timed(random_list)
    qs_it_rand = quicksort_iter_timed(random_list)

    expected_rand = sorted(random_list)
    assert ms_it_rand == qs_it_rand == expected_rand

    print("\n=== Уже отсортированный массив (худший случай для наших quicksort) ===")
    ms_it_sorted = mergesort_iter_timed(sorted_list)
    qs_it_sorted = quicksort_iter_timed(sorted_list)

    expected_sorted = sorted_list
    assert ms_it_sorted == qs_it_sorted == expected_sorted

    print("\n=== Обратный порядок (тоже плохой случай для quicksort с последним pivot) ===")
    ms_it_rev = mergesort_iter_timed(reversed_list)
    qs_it_rev = quicksort_iter_timed(reversed_list)

    expected_rev = sorted(reversed_list)
    assert ms_it_rev == qs_it_rev == expected_rev
