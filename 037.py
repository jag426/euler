from util import digits_10, primes

pg = primes()
ps = set()
ts = set()
while len(ts) < 11:
    p = next(pg)
    ps.add(p)
    if p >= 10 and all(map(
            lambda e: p % (10 ** e) in ps and p // (10 ** e) in ps,
            range(1, digits_10(p)))):
        ts.add(p)
print(sum(ts))
