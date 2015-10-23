from util import primes_to

primes = set(primes_to(10**6))
def rotate(n):
    s = str(n)
    return int(s[-1] + s[:-1])
def is_circular_prime(p):
    if not p in primes:
        return False
    r = rotate(p)
    while r != p:
        if not r in primes:
            return False
        r = rotate(r)
    return True
print(len(list(filter(is_circular_prime, primes))))
