#!/bin/python

# We are given a set of prices of an asset at certain time periods. We want
# to find out the least loss incurred if the asset it bought at time i and
# sold at time j. Thus, if P is the array of prices then find the negative
# of min(P[j] - P[i]).

def lag(X):
    """ Computes lag of an array. """
    Y = [0] * (len(X) - 1)

    for i in range(1, len(X)):
        Y[i-1] = X[i] - X[i - 1]

    return Y

def cumsum(X):
    """ Computes cumulative sum of an array. """
    Y = [X[0]] * len(X)

    for i in range(1, len(X)):
        Y[i] = Y[i - 1] + X[i]

    return Y

N = int(input())
raw_data = input()
prices = [int(p) for p in raw_data.split(' ')]

price_diff = lag(prices)
cumsums = [[]] * len(price_diff)
mindiffs = [0] * len(price_diff)

for i in range(len(price_diff)):
    cumsums[i] = cumsum(price_diff[i:])
    candidates = [m for m in cumsums[i] if m < 0]
    if (len(candidates) > 0):
        mindiffs[i] = max(candidates)

least_loss = -max([m for m in mindiffs if m < 0])
print(least_loss)

