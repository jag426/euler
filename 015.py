""" No combinatorics, because DP is fun! """

N, M = 21, 21
A = [x[:] for x in [[0]*N]*M]
A[0][0] = 1
for n in range(N):
    for m in range(M):
        if n:
            A[n][m] += A[n-1][m]
        if m:
            A[n][m] += A[n][m-1]
print(A[-1][-1])
