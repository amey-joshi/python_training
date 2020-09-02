#!/bin/python

def bday_candles(X):
    """ Count the # occurrences of the max element in X. """
    # A straightforward logic like:
    # len([X[i] for i in range(len(X)) if X[i] == max(X))
    # is quite slow.
    X = sorted(X, reverse = True)
    largest = X[0]
    count = 0
    for i in range(len(X)):
        if X[i] < largest:
            break
        else:
            count += 1

    return count

def main():
    n = int(input().strip())
    X = [int(n.strip()) for n in input().rstrip().split(' ')]

    print(bday_candles(X))

if __name__ == '__main__':
    main()

