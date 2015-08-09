def decimal_cycle(d):
    """ Compute the length of the repeating cycle in the decimal representation
        of 1/d for integer d >= 2.
    """

    rems = [1]
    while rems[-1] not in rems[:-1]:
        n = rems[-1]*10
        q = n//d
        r = n-q*d
        if r == 0:
            return 0
        rems.append(r)
    # rems[-1] appears exactly once in rems[:-1]
    return len(rems) - rems[:-1].index(rems[-1]) - 1

max_cycle = 0
max_d = 0
for d in range(2, 1000):
    cycle = decimal_cycle(d)
    if cycle > max_cycle:
        max_cycle, max_d = cycle, d
print(max_d)
