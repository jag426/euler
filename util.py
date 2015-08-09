def divisors(n):
    """A set of the proper divisors of n for any positive integer n.

    >>> divisors(1)
    {1}
    >>> divisors(17.0)
    {1}
    >>> divisors(4) == {1, 2}
    True
    >>> divisors(49) == {1, 7}
    True
    >>> divisors(120) == {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60}
    True
    >>> len(divisors(360))
    23
    >>> len(divisors(2520))
    47
    >>> divisors(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    >>> divisors(2**0.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    from functools import reduce
    from math import floor
    from util import powerset, prime_factorization
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if not n >= 1:
        raise ValueError("n must be positive")
    pf = prime_factorization(n)
    factor_sets = powerset(pf)
    product = lambda factors: reduce(lambda x,y: x*y, factors, 1)
    divisors = {product(factors) for factors in factor_sets}
    if n != 1:
        divisors.discard(n)
    return divisors

def powerset(iterable):
    """An iterable of iterables representing the powerset of the input iterable.
       Implementation taken from:
       https://docs.python.org/3/library/itertools.html#itertools-recipes

    >>> list(powerset([]))
    [()]
    >>> list(powerset([0]))
    [(), (0,)]
    >>> list(powerset([0, 1]))
    [(), (0,), (1,), (0, 1)]
    """

    from itertools import chain, combinations
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def prime_factorization(n):
    """A sorted list of the prime factors of n for any positive integer n.

    >>> prime_factorization(1)
    []
    >>> prime_factorization(2)
    [2]
    >>> prime_factorization(17.0)
    [17]
    >>> prime_factorization(49)
    [7, 7]
    >>> prime_factorization(360)
    [2, 2, 2, 3, 3, 5]
    >>> prime_factorization(1234567890987654321)
    [3, 3, 7, 19, 928163, 1111211111]
    >>> prime_factorization(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    >>> prime_factorization(2**0.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    from math import floor
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if not n >= 1:
        raise ValueError("n must be positive")
    if n == 1:
        return []
    prime_factorization = []
    d = 2
    while d <= floor(n**0.5):
        while n%d == 0:
            prime_factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        prime_factorization.append(n)
    return prime_factorization

if __name__ == "__main__":
    import doctest
    doctest.testmod()
