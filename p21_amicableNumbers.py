#!/usr/bin/env python3
from math import sqrt,ceil

def memoize(f):
    cache = {}
    def mem(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return mem

@memoize
def d(n):
    count = 1
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0:
            count += i
            count += n//i
    return count

def amicablePairsUnder(n):
    pairs = []
    for i in range(2,n):
        if i not in pairs:
            for j in range(i+1,n):
                if d(i) == j and d(j) == i:
                    print("d({})={},d({})={}".format(i,d(i),j,d(j)))
                    pairs.append(i)
                    pairs.append(j)
    return sum(pairs)

print(amicablePairsUnder(10000))
