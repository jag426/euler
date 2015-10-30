from itertools import product

print(max(map(lambda n: sum([int(c) for c in str(n)]), [a**b for a, b in product(range(100), repeat=2)])))
