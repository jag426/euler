n = 1
sum = 1
for s in range(2, 1001, 2):
    for i in range(4):
        n += s
        sum += n
print(sum)
