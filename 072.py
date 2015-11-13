phis = list(range(10**6+1))
for i in range(2, 10**6+1):
    if phis[i] == i:
        for m in range(i, 10**6+1, i):
            phis[m] = phis[m] * (i-1) // i
print(sum(phis[2:]))
