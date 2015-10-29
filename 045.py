from itertools import count
from util import is_pentagonal

def nth_triangle(n):
    return n * (n + 1) // 2

# every other triangle number is hexagonal
for n in count(287, 2):
    t = nth_triangle(n)
    if is_pentagonal(t):
        print(t)
        break
