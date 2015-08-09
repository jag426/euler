def divisors(n):
    """A set of the proper divisors of n for any positive integer n.
       O(sqrt(n)).

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

    from math import floor
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if not n >= 1:
        raise ValueError("n must be positive")
    divisors = {1}
    for d in range(2, floor(n**0.5)+1):
        if n%d == 0:
            divisors |= {d, n//d}
    return divisors

def prime_factors(n):
    """A sorted list of the prime factors of n for any positive integer n.

    >>> prime_factors(1)
    []
    >>> prime_factors(2)
    [2]
    >>> prime_factors(17.0)
    [17]
    >>> prime_factors(49)
    [7, 7]
    >>> prime_factors(360)
    [2, 2, 2, 3, 3, 5]
    >>> prime_factors(1234567890987654321)
    [3, 3, 7, 19, 928163, 1111211111]
    >>> prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    >>> prime_factors(2**0.5)
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
    prime_factors = []
    d = 2
    while d <= floor(n**0.5):
        while n%d == 0:
            prime_factors.append(d)
            n //= d
        d += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

if __name__ == "__main__":
    import doctest
    doctest.testmod()
