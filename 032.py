""" For a given permutation of the digits 1-9 (call it abcdefghi), we only need
    to check two ways it could be split into a valid multiplication:
        a * bcde = fghi
        ab * cde = fghi
    You might think to check abc * de = fghi and abcd * e = fghi, but those are
    already covered by other permutations (deabcfghi and eabcdfghi).
    So we iterate over the permutations of the digits 1-9, for each one checking
    if these multiplications hold. Fortunately, there are only 9! permutations,
    so it doesn't take long.
"""

from itertools import permutations

products = set()
for p in permutations('123456789'):
    product = int(''.join(p[5:]))
    a = int(''.join(p[:1]))
    b = int(''.join(p[1:5]))
    c = int(''.join(p[:2]))
    d = int(''.join(p[2:5]))
    if a*b == product or c*d == product:
        products.add(product)
print(sum(products))
