from itertools import product
print(max([x*y for (x, y) in product(range(100, 1000), repeat=2) if str(x*y) == str(x*y)[::-1]]))
