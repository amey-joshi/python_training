#!/bin/python

def min_max_sum(X):
    assert len(X) == 5

    sums = [0] * len(X) 
    for i in range(5):
        sums[i] = int(sum(X[j] * 1.0 for j in range(5) if j != i))

    return [min(sums), max(sums)]

def main():
    X = [int(x.strip()) for x in input().rstrip().split(' ')]
    l, h = min_max_sum(X)
    print(f'{l} {h}')

if __name__ == '__main__':
    main()

