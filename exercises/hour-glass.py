#!/bin/python

# An hourglass in a 2-d array is a set of values arranged in the array as
#                              a b c
#                                d
#                              d e f
# An hourglass sum is the sum of elements forming an hourglass. Find the 
# maximum hourglass sum.

def hg_sum(i, j, m, n, A):
    s = 0
    if ((i + 2 < m ) and (j + 2 < n)):
        s += A[i][j] + A[i][j+1] + A[i][j+2] 
        s += A[i+1][j+1] 
        s += A[i+2][j] + A[i+2][j+1] + A[i+2][j+2]

    return s
   
N = 6
A = [[0] * N] * N

for i in range(N):
    line = input()
    A[i] = [int(n) for n in line.split(' ')]

hg_sums = []
for i in range(N):
    for j in range(N):
        hg_sums.append(hg_sum(i, j, N, N, A))

print(max(hg_sums))

