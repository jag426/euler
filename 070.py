"""We want as few and as large prime factors as possible in order to maximize
   phi(n) and minimize n/phi(n). But n can't be prime (phi(n) would be n-1 which
   is never a permutation of n), so try products of two primes instead."""

from util import primes
import sys

def is_permutation(n, m):
    return sorted(str(n)) == sorted(str(m))

best_ratio = sys.maxsize
best_n = None
pg = primes()
primes = []
for p in pg:
    if p > 10**7//2:
        break
    for q in primes:
        n = p*q
        if n > 10**7:
            break
        phi = (p-1)*(q-1)
        ratio = n/phi
        if ratio < best_ratio and is_permutation(n, phi):
            best_n = n
            best_ratio = ratio
    primes.append(p)
print(best_n)
