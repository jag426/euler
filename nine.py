print(next(a*b*c for a in range(1, 1000) for b in range(1, 1000-a) for c in [1000-a-b] if a**2 + b**2 == c**2))
