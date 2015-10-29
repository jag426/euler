from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
print(sum([int(''.join(p)) for p in permutations('0123456789') if all([int(''.join(p[i+1:i+4])) % primes[i] == 0 for i in range(7)])]))
