from itertools import count

total = 0
for e in count(1):
    add = len([0 for b in range(1, 10) if len(str(b**e)) == e])
    total += add
    if add == 0:
        break
print(total)
