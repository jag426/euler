from itertools import permutations

for s in permutations('987654321', r=4):
    s = ''.join(s)
    product = s + str(int(s)*2)
    if set(product) == set('987654321'):
        print(product)
        break
