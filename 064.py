from math import floor, sqrt

def period(N):
    mda = []
    m = 0
    d = 1
    a = floor(sqrt(N))
    while (m, d, a) not in mda:
        mda.append((m, d, a))
        m = d * a - m
        d = (N - m*m) // d
        if d == 0: # N is a square
            return 0
        a = floor((sqrt(N) + m) / d)
    return len(mda) - mda.index((m, d, a))

print(len([N for N in range(10001) if period(N) % 2 == 1]))
