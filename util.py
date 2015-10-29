def digits_10(n):
    """The number of digits in the decimal representation of any integer n, not
       including the - sign.

    >>> digits_10(0)
    1
    >>> digits_10(199)
    3
    >>> digits_10(-12)
    2
    >>> digits_10(0.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    from math import floor, log10
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if n == 0:
        return 1
    return int(log10(abs(n))) + 1

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

def gcd(a, b):
    """Return the greatest common divisor of a and b for integers a and b not
       both 0.

    >>> gcd(54, 24)
    6
    >>> gcd(48, -180)
    12
    >>> gcd(-37, 600)
    1
    >>> gcd(-13, -13)
    13
    >>> gcd(20, 100)
    20
    >>> gcd(624129, 2061517)
    18913
    >>> gcd(0, 6)
    6
    >>> gcd(6, 0)
    6
    >>> gcd(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: a or b must not be 0
    >>> gcd(5.5, 11)
    Traceback (most recent call last):
        ...
    ValueError: a must be an integer
    >>> gcd(0, 1.5)
    Traceback (most recent call last):
        ...
    ValueError: b must be an integer
    """

    from math import floor
    if floor(a) != a:
        raise ValueError("a must be an integer")
    a = floor(a)
    if floor(b) != b:
        raise ValueError("b must be an integer")
    b = floor(b)
    if a == 0 and b == 0:
        raise ValueError("a or b must not be 0")
    while b != 0:
        a, b = b, a % b
    return abs(a)

def is_prime(n):
    """Naive primality test. Return whether n is prime for integer n >= 2.

    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(655559.0)
    True
    >>> is_prime(655559*655559)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    from math import floor
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if not n >= 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for d in range(3, floor(n**0.5)+1, 2):
        if n%d == 0:
            return False
    return True

def is_triangle(n):
    """Return whether n is a triangle number for integer n >= 0.
       n is a triangle number iff 8n+1 is a square.

    >>> is_triangle(0)
    True
    >>> is_triangle(1)
    True
    >>> is_triangle(16)
    False
    >>> is_triangle(15)
    True
    >>> is_triangle(500500)
    True
    >>> is_triangle(499513)
    False
    >>> is_triangle(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be non-negative
    >>> is_triangle(2.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    from math import floor, sqrt
    if floor(n) != n:
        raise ValueError("n must be an integer")
    n = floor(n)
    if not n >= 0:
        raise ValueError("n must be non-negative")
    x = 8 * n + 1
    return sqrt(x) == floor(sqrt(x))

def postponed_sieve():
    """A prime generator from http://stackoverflow.com/a/10733621."""

    from itertools import count
    yield 2; yield 3; yield 5; yield 7;
    sieve = {}
    ps = postponed_sieve()
    p = next(ps) and next(ps)
    q = p*p
    for c in count(9, 2):
        if c in sieve:
            s = sieve.pop(c)
        elif c < q:
            yield c
            continue
        else: # c == q
            s = count(q + 2 * p, 2 * p)
            p = next(ps)
            q = p * p
        for m in s:
            if m not in sieve:
                break;
        sieve[m] = s

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

primes = postponed_sieve

def primes_to(n):
    """Generate primes up to n."""

    p = primes()
    next_prime = next(p)
    while next_prime <= n:
        yield next_prime
        next_prime = next(p)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
