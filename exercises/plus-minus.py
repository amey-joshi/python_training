#!/bin/python
import numpy as np

def plus_minus(X):
    d = len(X)
    X = np.array(X)

    p = len(X[X > 0])/d
    n = len(X[X < 0])/d
    z = len(X[X == 0])/d

    return (p, n, z)

def plus_minus_bare(X):
    d = len(X)

    p = len([1 for n in X if n > 0])/d
    n = len([1 for n in X if n < 0])/d
    z = len([1 for n in X if n == 0])/d

    return (p, n, z)

def main():
    n = int(input().strip())
    X = [int(n.strip()) for n in input().rstrip().split(' ')]
    p, n, z = plus_minus(X)

    print(f'{p:.6f}')
    print(f'{n:.6f}')
    print(f'{z:.6f}')

if __name__ == '__main__':
    main()


