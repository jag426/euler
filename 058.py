from itertools import count
from util import is_prime

n = 1
p = 0
t = 1
for s in count(2, 2):
    for i in range(4):
        n += s
        p += is_prime(n)
        t += 1
    if p/t < 0.1:
        print(s+1)
        break
