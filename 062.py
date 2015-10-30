from itertools import count

# sorted string rep -> [first cube, # of cubes]
cubes = {}

for n in count():
    c = n**3
    rep = ''.join(sorted(str(c)))
    if rep in cubes:
        cubes[rep][1] += 1
    else:
        cubes[rep] = [c, 1]
    if cubes[rep][1] == 5:
        print(cubes[rep][0])
        break
