def is_palindrome(n):
    return str(n) == str(n)[::-1]

def flip(n):
    return int(str(n)[::-1])

def is_lychrel(n, limit=50):
    if not limit > 0:
        return True
    m = n + flip(n)
    if is_palindrome(m):
        return False
    return is_lychrel(m, limit - 1)

print(len([n for n in range(10**4) if is_lychrel(n)]))
