import random

def partition(nums, left, right, pivot_index):
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left

    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    nums[store_index], nums[right] = nums[right], nums[store_index]
    return store_index


def find_kth_largest(nums, k):
    left, right = 0, len(nums) - 1
    target = len(nums) - k

    while True:
        pivot_index = random.randint(left, right)
        pivot_index = partition(nums, left, right, pivot_index)

        if pivot_index == target:
            return nums[pivot_index]
        elif pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
