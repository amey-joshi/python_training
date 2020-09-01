#!/bin/python

# Calculate the weighted mean of data. The input consists of three lines, 1)
# the number of elements in the data, 2) a line containing space separated
# integers and 3) a line containing space separated weights.

N = int(input())
X = input()
W = input()

X = [int(x) for x in X.split(' ')]
W = [int(w) for w in W.split(' ')]

if N != len(X):
    print(f'Expected {N} numbers, got {len(X)}')
    exit(-1)

if N != len(W):
    print(f'Expected {N} weights, got {len(W)}')
    exit(-2)


tot = 0.0
for i in range(len(X)):
    tot += X[i] * W[i]
wm = tot/sum(W)

print(round(wm, 1))

