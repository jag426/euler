import math

def is_amicable(n):
    def d(n):
        sum = 1
        for d in range(2, math.floor(n**0.5)+1):
            if n%d==0:
                sum += d
                if n//d != d:
                    sum += n//d
        return sum
    return d(n) != n and d(d(n)) == n

print(sum(filter(is_amicable, range(1, 10000))))
