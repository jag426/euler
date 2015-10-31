from util import gcd

n = 3
d = 2
ans = 0
for i in range(1, 1000):
    n, d = n + 2*d, n + d
    g = gcd(n, d)
    n //= g
    d //= g
    if len(str(n)) > len(str(d)):
        ans += 1
print(ans)
