from math import ceil
from util import gcd

fractions = set()
for d in range(2, 12001):
    print(d)
    for n in range(d//3 + 1, ceil(d/2)):
        g = gcd(n, d)
        fractions.add((n//g, d//g))
print(len(fractions))
