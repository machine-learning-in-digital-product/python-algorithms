def two_sum_indices(arr, k):
    idx_of: dict[int, int] = {}
    for j, x in enumerate(arr):
        need = k - x
        if need in idx_of:
            i = idx_of[need]
            return (i, j) if i < j else (j, i)
        idx_of[x] = j
    raise ValueError("No valid pair found")
