def num_divisors(n):
    count = 2
    sqrt = n**0.5
    limit = int(sqrt)
    if limit == sqrt:
        count = count + 1
    for d in range(2, limit):
        if n%d == 0:
            count = count + 2
    return count

def triangle_numbers():
    n = 1
    current = 1
    while 1:
        yield current
        n = n + 1
        current = current + n

for t in triangle_numbers():
    if num_divisors(t) >= 500:
        print(t)
        break
