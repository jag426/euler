from itertools import count

for n in count(1):
    digits = set(str(n))
    same_digits = lambda m: set(str(m)) == digits
    if all(map(same_digits, [i*n for i in range(2, 7)])):
        print(n)
        break
