def fib_even(n):
  x, y = 1, 2
  while y <= n:
    yield y
    z = x + y
    x = y + z
    y = x + z

print(sum(fib_even(4000000)))
