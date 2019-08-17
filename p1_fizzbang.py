#!/usr/bin/env python3
import math
import time
# problem 1
# Find the sum of all the multiples of 3 or 5 below 1000
def fizzbang(n):
    list = []
    for i in range(n):
        if i % 3 == 0:
            list.append(i)
        elif i % 5 == 0:
            list.append(i)
    return sum(list)
