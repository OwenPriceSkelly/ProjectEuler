#!/usr/bin/env python3
from time import time

def memoize(f):
    cache = {}
    def memo(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return memo

@memoize
def collatz(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + collatz(n//2)
    else:
        return 1 + collatz(3*n + 1)

t0 = time()
max = 0
max_starting = 1
limit = 1000000
for i in range(1,limit):
    if collatz(i) > max:
        max = collatz(i)
        max_starting = i
print("The longest chain under {} is {}, starting at  {}".format(limit,max,max_starting))
print(time() - t0)
