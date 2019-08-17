#!/usr/bin/env python3
import math
import time
# problem 5
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
def leastCommonMultiple(n):
    x = 1
    for i in range(1,n):
        x = x*i//math.gcd(x,i)
    return x
