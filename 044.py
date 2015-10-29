from itertools import count

nth = lambda n: n * (3*n - 1) // 2
ps = set()
done = False
n = 0
while not done:
    n += 1
    pn = nth(n)
    ps.add(pn)
    for p in ps:
        if pn - p in ps and pn - 2*p in ps:
            print(pn - 2*p)
            done = True
            break
