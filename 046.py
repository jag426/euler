from itertools import count
from math import floor, sqrt
from util import is_prime

for n in count(3, 2):
    if not any(map(is_prime, [n - 2*i*i for i in range(floor(sqrt(n/2)) + 1)])):
        print(n)
        break
