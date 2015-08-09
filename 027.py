from util import is_prime

max_primes = 0
max_a, max_b = None, None
for a in range(-999, 1000):
    for b in range(2, 1000): # b must be prime, no use checking b<2
        n = 0
        while is_prime(n*n + n*a + b):
            n += 1
        if n > max_primes:
            max_primes, max_a, max_b = n, a, b
print(max_a*max_b)
