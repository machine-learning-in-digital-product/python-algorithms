import random

from kth import find_kth_largest

def test_examples():
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    assert find_kth_largest(nums1.copy(), k1) == 5

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    assert find_kth_largest(nums2.copy(), k2) == 4


def test_with_duplicates():
    nums = [5, 3, 5, 2, 5, 1, 4]
    sorted_desc = sorted(nums, reverse=True)

    for k in range(1, len(nums) + 1):
        expected = sorted_desc[k - 1]
        result = find_kth_largest(nums.copy(), k)
        assert result == expected, f"k={k}: expected {expected}, got {result}"


def test_negative_numbers():
    nums = [-1, -5, 0, 3, -2]
    sorted_desc = sorted(nums, reverse=True)

    for k in range(1, len(nums) + 1):
        expected = sorted_desc[k - 1]
        result = find_kth_largest(nums.copy(), k)
        assert result == expected, f"k={k}: expected {expected}, got {result}"


def random_tests(num_tests=100, max_len=50, value_range=(-1000, 1000)):
    for _ in range(num_tests):
        length = random.randint(1, max_len)
        nums = [random.randint(*value_range) for _ in range(length)]
        k = random.randint(1, length)

        sorted_desc = sorted(nums, reverse=True)
        expected = sorted_desc[k - 1]
        result = find_kth_largest(nums.copy(), k)

        assert result == expected, f"nums={nums}, k={k}, expected={expected}, got={result}"


if __name__ == "__main__":
    test_examples()
    test_with_duplicates()
    test_negative_numbers()
    random_tests()

    print("All tests passed!")
