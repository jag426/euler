dens = [2]
i = 1
while len(dens) < 100:
    dens.extend([1, 2*i, 1])
    i += 1
dens = dens[::-1]
# dens == [2, 1, 2, 1, 1, 4, 1, ..., 1, 66, 1]

n = dens[0]
d = 1
for i in dens[1:]:
    n, d = i*n + d, n
print(sum([int(d) for d in str(n)]))
