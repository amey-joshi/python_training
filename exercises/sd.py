#!/bin/python
import math

N = int(input())
line = input()
X = [int(n) for n in line.split(' ')]

def mean(X):
    return sum(X)/len(X)

n = sum([(n - mean(X))**2 for n in X])
v = n/len(X)
s = math.sqrt(v)

print(round(s, 1))
