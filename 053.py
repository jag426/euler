from math import factorial

def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

print(len([0 for n in range(101) for k in range(n+1) if choose(n, k) > 10**6]))
