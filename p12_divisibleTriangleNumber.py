#!/usr/bin/env python3
# The sequence of triangle numbers is generated by adding
# the natural numbers. So the 7th triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt,ceil
import time

def divisibleTriangleNumber(min_divisors):
    n = 1
    while True:
        num = n*(n+1)//2
        if numDivisors(num) > min_divisors:
            return num
        else: n += 1

def numDivisors(n):
    count = 0
    for i in range(1,ceil(sqrt(n))):
        if n % i == 0: count += 2
        if i * i == n: count -= 1
    return count
    
t0 = time.time()
print(divisibleTriangleNumber(500))
print(time.time()-t0)
