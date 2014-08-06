from functools import reduce
primes = [2, 3, 5, 7, 11, 13, 17, 19]
ns = list(range(1,21))
ms = []
for p in primes:
  def div(i):
    c = 0
    n = ns[i]
    while n%p == 0:
      n /= p
      c += 1
    ns[i] = n
    return c
  ms.append(max(map(div, range(len(ns)))))
print(reduce(lambda x, y : x*y, [x**y for (x, y) in zip(primes, ms)]))
