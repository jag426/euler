n = 10001
primes = []
i = 2
while len(primes) < n:
  for p in primes:
    if i%p == 0:
      break
  else:
    primes.append(i)
  i += 1
print(primes[-1])
