target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
combinations = [0] * (target + 1)
combinations[0] = 1
for coin in coins:
    for value in range(coin, len(combinations)):
        combinations[value] += combinations[value - coin]
print(combinations[-1])
