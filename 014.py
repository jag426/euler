# steps[n] is the steps required for n, or 0 if not yet computed
steps = {1: 0}

def count(n):
    if n not in steps:
        if n%2==0:
            steps[n] = 1 + count(n//2)
        else:
            steps[n] = 1 + count(3*n+1)
    return steps[n]

best_n, best_count = 0, 0

for n in range(2, 1000000):
    c = count(n)
    if c > best_count:
        best_n, best_count = n, c

print(best_n)
