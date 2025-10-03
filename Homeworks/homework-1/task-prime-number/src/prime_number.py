import math

def count_primes_below(n: int) -> int:
    if n <= 2:
        return 0
    
    primes = [True] * n
    primes[0] = primes[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False

    simple_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return len(simple_numbers)

print(count_primes_below(3))
