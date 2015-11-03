from math import floor, sqrt

def frac(alist):
    if len(alist) < 1:
        return None
    if len(alist) == 1:
        return (alist[0], 1)
    n, d = frac(alist[1:])
    return d + alist[0]*n, n

def solved(D, xy):
    x, y = xy
    return x*x - D*y*y == 1

def x(D):
    m = 0
    d = 1
    a = floor(sqrt(D))
    alist = [a]
    while not solved(D, frac(alist)):
        m = d * a - m
        d = (D - m * m) // d
        a = floor((sqrt(D) + m) / d)
        alist.append(a)
    return frac(alist)[0]

print(max([(x(D), D) for D in range(1001) if round(sqrt(D))**2 != D])[1])
