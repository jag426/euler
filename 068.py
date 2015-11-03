from itertools import combinations, permutations

best = ''
values = list(range(1, 11))
for a in range(1, 7):
    for comb in combinations(range(a+1, 10), r=3):
        rest = [v for v in values if v not in [a, 10] and v not in comb]
        for f, g, h, i, j in permutations(rest, r=5):
            rest = [v for v in values if v not in [a, f, g, h, i, j]]
            for b, c, d, e in permutations(rest):
                total = a+f+g
                magic = all([x+y+z==total for x, y, z in [
                    (b, g, h), (c, h, i), (d, i, j), (e, j, f)
                ]])
                if magic:
                    s = ''.join([str(v) for v in [
                        a, f, g, b, g, h, c, h, i, d, i, j, e, j, f
                    ]])
                    if s > best:
                        best = s
print(best)
