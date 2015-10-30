from util import is_prime

def is_permutation(x, y):
    xs, ys = list(str(x)), list(str(y))
    xs.sort(); ys.sort()
    return xs == ys

for i in range(1001, 10000, 2):
    if is_prime(i):
        for d in range(2, (10001 - i) // 2, 2):
            if is_permutation(i, i + d) and is_permutation(i, i + 2*d) and is_prime(i + d) and is_prime(i + 2*d):
                print(str(i) + str(i + d) + str(i + 2*d))
