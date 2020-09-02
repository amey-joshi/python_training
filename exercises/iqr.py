#!/bin/python

N = int(input())
X = [int(x) for x in input().split(' ')]
F = [int(f) for f in input().split(' ')]

def build_data(X, F):
    S = []
    for i in range(N):
        for j in range(F[i]):
            S.append(X[i])

    S.sort()
    return S

def median(Y):
    """ Assume that Y is sorted. """
    b = len(Y) // 2
    
    if len(Y) % 2 == 0:
        return round((Y[b-1] + Y[b])/2, 1)
    else:
        return round(Y[b], 1)


S = build_data(X, F)

if len(S) % 2 == 0:
    q1 = median(S[0:(len(S)//2)])
    q3 = median(S[(len(S)//2):])
else:
    q1 = median(S[0:(len(S)//2)])
    q3 = median(S[(len(S)//2 + 1):])

print(q3 - q1)
