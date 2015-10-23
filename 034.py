from math import factorial

limit = 2540160 # 7 * 9!
def is_digit_factorial_sum(x):
    return x == sum(map(lambda d: factorial(int(d)), str(x)))
print(sum(filter(is_digit_factorial_sum, range(10, limit + 1))))
