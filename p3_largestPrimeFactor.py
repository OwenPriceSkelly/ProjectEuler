#!/usr/bin/env python3
import math
import time
# problem 3
# What is the largest prime factor of the number
# 600851475143?
def largestPrimeFactor(n):
    i=2
    while (i * i <= n):
        while(n % i == 0):
            if n <= i: break
            n = n//i
        i = i + 1
    return n
