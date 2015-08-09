""" free arbitrary-precision ints are cheaing. :D """

index = 1
prev = 0
curr = 1
while len(str(curr)) < 1000:
    curr, prev = curr + prev, curr
    index += 1
print(index)
