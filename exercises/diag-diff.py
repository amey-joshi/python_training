#!/bin/python

def diagonal_difference(M):
    """ Computes the absolute difference between sum of diagonal elements."""
    assert len(M) == len(M[0])

    # The trace.
    ms = sum(M[i][i] for i in range(len(M)))

    # Sum of the elements of the other diagonal.
    ss = 0
    n = len(M)
    for i in range(len(M)):
        ss += M[n - 1 - i][i]

    return abs(ss - ms)

def main():
    n = int(input().strip())
    M = [] # the matrix to be built
    for i in range(n):
        M.append([int(n.strip()) for n in input().rstrip().split(' ')])

    d = diagonal_difference(M)
    print(d)

if __name__ == '__main__':
    main()

