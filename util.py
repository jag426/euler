def divisors(n):
    """A set of the proper divisors of n for any positive integer n.
       O(sqrt(n)).
    >>> divisors(1)
    {1}
    >>> divisors(17)
    {1}
    >>> divisors(4) == {1, 2}
    True
    >>> divisors(49) == {1, 7}
    True
    >>> divisors(120) == {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60}
    True
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
    if not n >= 1:
        raise ValueError("n must be positive")
    if floor(n) != n:
        raise ValueError("n must be an integer")
    divisors = {1}
    for d in range(2, int(n**0.5)+1):
        if n%d == 0:
            divisors |= {d, n//d}
    return divisors

if __name__ == "__main__":
    import doctest
    doctest.testmod()
