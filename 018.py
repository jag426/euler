lines = open('p018.txt').readlines()
rows = list(map(lambda line: list(map(int, line.split())), lines))

# iterate over the rows in reverse order, starting with the second to last
for i in range(len(rows)-2, -1, -1):
    row = rows[i]
    # replace each member of the row with the value of the max path from there
    # to the bottom
    for j in range(len(row)):
        row[j] += max(rows[i+1][j], rows[i+1][j+1])

print(rows[0][0])
