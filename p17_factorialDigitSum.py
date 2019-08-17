#!/usr/bin/env python3

# find the sum of the digits of 100!

def memoize(f):
    cache = {}
    def mem(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return mem

@memoize
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

fact_string = str(factorial(100))
digits = [int(x) for x in fact_string]
print(fact_string)
print(sum(digits))
