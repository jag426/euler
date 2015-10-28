def ppd():
    "pandigital primes descending"
    from itertools import permutations
    from math import floor
    from util import is_prime
    
    for n in range(0, 9):
        digits = '987654321'[n:]
        if sum(map(int, digits)) % 3 == 0:
            # every permutation will be divisible by 3
            continue
        for p in permutations(digits):
            x = int(''.join(p))
            if is_prime(x):
                yield x

print(next(ppd()))
