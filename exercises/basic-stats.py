#!/bin/python

# Read two lines from the standard input 1) a positive integer, N, and 2) a 
# line with N other integers. Find the mean, median and mode of the data 
# entered on the second line.

import numpy as np

N = int(input())
line = input()
X = [int(x) for x in line.split(' ')]

if N != len(X):
    print(f'Expected {N} numbers, got {len(X)}')
    exit(-1)

mid = int(len(X)/2)
mean = sum(X)/N

X.sort()
if N % 2 == 0:
    median = (X[mid - 1] + X[mid])/2
else:
    median = X[mid]

S = set(x for x in X) # Set of elements in X
U = [x for x in S]    # Unique elements in X
U.sort()
F = [1] * len(U)      # Frequencies of elements in X

if len(U) == len(X): # There are no duplicates.
    mode = X[0]
else:
    j = 0 # index in X
    for i in range(len(U)):
        f = 0
        while j < len(X) and U[i] == X[j]:
            j += 1
            f += 1
        F[i] = f

mode = U[np.argmax(F)]

print(mean)
print(median)
print(mode)

