from util import is_prime, primes

pg = primes()
while next(pg) <= 56003:
    pass
answer = None
for p in pg:
    s = str(p)
    for d in range(3):
        if str(d) in s:
            n = 1
            for e in range(d+1, 10):
                if is_prime(int(s.replace(str(d), str(e)))):
                    n += 1
            if n >= 8:
                answer = p
                break
    if answer:
        break
print(answer)
