#!/usr/bin/env python3
from time import time

# functions
def memoize(f):
    cache = {}
    def mem(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return mem

@memoize
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# run
t0 = time()
i=0
while True:
    i+=1
    if len(str(fib(i))) >= 1000:
        print(i)
        break
print(time() - t0)
