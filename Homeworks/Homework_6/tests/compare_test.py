import functools
import random
import sys
import time

from Compare import mergesort, quicksort


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
def mergesort_timed(arr):
    return mergesort(list(arr))

@measure_time
def quicksort_timed(arr):
    return quicksort(list(arr))

if __name__ == "__main__":
    sys.setrecursionlimit(50_000)

    n = 20_000

    random_list = [random.randint(0, 1_000_000) for _ in range(n)]
    sorted_list = list(range(n))
    reversed_list = list(range(n, 0, -1))

    print("=== Случайные данные ===")
    ms_random = mergesort_timed(random_list)
    qs_random = quicksort_timed(random_list)
    assert ms_random == qs_random == sorted(random_list)

    print("\n=== Уже отсортированный массив (худший случай для нашего quicksort) ===")
    ms_sorted = mergesort_timed(sorted_list)
    qs_sorted = quicksort_timed(sorted_list)
    assert ms_sorted == qs_sorted == sorted_list

    print("\n=== Обратный порядок (тоже плохой случай для такого quicksort) ===")
    ms_rev = mergesort_timed(reversed_list)
    qs_rev = quicksort_timed(reversed_list)
    assert ms_rev == qs_rev == sorted(reversed_list)
