def max_even_sum(arr):
    total = sum(arr)
    if total % 2 == 0:
        return total
    
    min_odd_number = None
    for current_number in arr:
        if (current_number % 2 == 1):
            if (min_odd_number is None):
                min_odd_number = current_number
            else:
                min_odd_number = min(current_number, min_odd_number)

    if not min_odd_number:
        return 0
    
    return total - min_odd_number
