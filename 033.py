from functools import reduce
from util import gcd

def is_cancelling(frac):
    (n, d) = frac
    if n % 10 == 0 or d % 10 == 0:
        return False
    if n % 10 == d % 10:
        return (n // 10) / (d // 10) == n / d
    if n % 10 == d // 10:
        return (n // 10) / (d % 10) == n / d
    if n // 10 == d % 10:
        return (n % 10) / (d // 10) == n / d
    if n // 10 == d // 10:
        return (n % 10) / (d // 10) == n / d
    return False

fracs = [(n, d) for n in range(10, 100) for d in range(n+1, 100)]
cancelling_fracs = filter(is_cancelling, fracs)
n, d = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), cancelling_fracs)
print(d // gcd(n, d))
