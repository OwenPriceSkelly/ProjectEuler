#!/usr/bin/env python3
import math

def memo(f):
    cache = []
    def memoize(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return memoize

@memo
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)




def result(n=4000000):
    """
    Problem 2
    By considering the terms in the Fibonacci sequence whose
    values do not exceed four million, find the sum of the
    even-valued terms.
    """
    i = sum = 0
    while fib(i) < n:
        if fib(i) % 2 == 0:
            sum += fib(i)
        i += 1
    return sum  
