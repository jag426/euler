from itertools import count
from util import prime_factors

for n in count(2*3*5*7):
    if all(map(lambda i: len(prime_factors(n+i)) == 4, range(4))):
        print(n)
        break
