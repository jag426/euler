sieve = [1]*2000000
sieve[0] = 0
sieve[1] = 0
for n in range(int(len(sieve)**0.5)):
    if sieve[n]:
        for multiple in range(2*n, len(sieve), n):
            sieve[multiple] = 0
print(sum(map(lambda x: x[0], filter(lambda x: x[1], enumerate(sieve)))))
