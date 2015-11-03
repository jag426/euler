from util import primes

product = 1
for p in primes():
    next = product * p
    if next > 10**6:
        break
    product = next
print(product)
