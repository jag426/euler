from util import divisors

limit = 28124
abundant = lambda n: sum(divisors(n)) > n

non_abundant_sums = set(range(1, limit))
abundants = set()
for n in range(1, limit):
    if abundant(n):
        abundants.add(n)
        for a in abundants:
            non_abundant_sums.discard(n+a)
print(sum(non_abundant_sums))
