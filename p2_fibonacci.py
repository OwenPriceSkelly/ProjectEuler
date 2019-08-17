#!/usr/bin/env python3
import math
import time
# problem 2
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the
# even-valued terms.
def fib(x,y,n,evens):
    z = x + y
    if z >= n:
        return
    if z % 2 == 0:
        evens.append(z)
    fib(y,z,n,evens)
