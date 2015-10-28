champernowne = ''
n = 0
while len(champernowne) < 1000001:
    champernowne += str(n)
    n += 1
product = 1
for e in range(1, 7):
    product *= int(champernowne[10**e])
print(product)
