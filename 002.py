def fib_even(n):
  """
  Generate the even Fibonacci numbers up to n.
  
  Every third Fibonacci number is even. This is easy to see by induction:
    odd+odd=even
    odd+even=odd
    even+odd=odd
  
  We can easily compute the n+2th and n+3th Fibonacci numbers using the
  n-1th and nth. y is the nth Fibonacci number, and x is the n-1th.
  
  Examine an iteration of the generator. Think of y as f_n and x as f_{n-1}
  at the beginning of an iteration.
    z = x + y = f_{n-1} + f_n     = f_{n+1}
    x = y + z = f_n +     f_{n+1} = f_{n+2}
    y = x + z = f_{n+2} + f_{n+1} = f_{n+3}
  Thus, an iteration advances x and y by 3 steps in the Fibonacci sequence.
  Since y and x start as 2 and 1 (the first even Fibonacci number and the
  Fibonacci number preceding it), the correctness of this generator follows.
  """
  x, y = 1, 2
  while y <= n:
    yield y
    z = x + y
    x = y + z
    y = x + z

print(sum(fib_even(4000000)))
