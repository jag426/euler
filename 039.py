from math import floor

# if a*a + b*b == c*c and a + b + c == p then b = (p*p - 2*p*a)/(2*p - 2*a) and
# p must be even.
max_solutions = 0
max_p = 0
for p in range(4, 1001, 2):
    solutions = 0
    a = 1
    while True:
        b = p*(p-2*a)/2/(p-a)
        if floor(b) == b:
            solutions += 1
        if a > b:
            break
        a += 1
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p
print(max_p)
