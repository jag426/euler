from util import primes as pg

# primes[i] = (i)th prime
primes = [0]
# sums[i] = sum of the first i primes
sums = [0]

# populate primes and sums
for p in pg():
    if p > 10**6:
        break
    primes.append(p)
    sums.append(sums[-1] + p)

# search for the prime under 10**6 with the most summands
done = False
for num_summands in range(len(primes) - 1, 0, -1):
    if done:
        break
    for bottom in range(len(sums) - num_summands):
        top = bottom + num_summands
        sum = sums[top] - sums[bottom]
        if sum > 10**6:
            break
        if sum in primes:
            print(sum)
            done = True
            break
