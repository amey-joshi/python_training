#!/bin/python

N = int(input())
line = input()
X = [int(n) for n in line.split(' ')]

def median(Y):
    """ Assume that Y is sorted. """
    l = len(Y)
    if l % 2 == 0:
        m = (Y[l//2 - 1] + Y[l//2])/2
    else:
        m = Y[l // 2]

    return m

X.sort()
q2 = median(X)
size = len(X)

if size % 2 == 0:
    b = int(size/2)
    q1 = median(X[0:b])
    q3 = median(X[b:])
else:
    q1 = median(X[0:(size//2)])
    q3 = median(X[(size//2 + 1):])

print(int(q1))
print(int(q2))
print(int(q3))

