from math import floor
from util import gcd

best_n, best_d = 0, 1
for d in range(1, 10**6+1):
    n = floor(d*3/7)
    if n*7 == d*3:
        n -= 1
    if n/d > best_n/best_d:
        best_n, best_d = n, d
print(best_n // gcd(best_n, best_d))
