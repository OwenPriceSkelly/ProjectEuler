#!/usr/bin/env python3
import math
import time
# problem 6
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
def sumSquaresDifference(n):
    sumOfSquares = n*(n+1)*(2*n+1)//6
    squareOfSum = (n*(n+1)//2)**2
    return squareOfSum - sumOfSquares

t0 = time.time()
print(sumSquaresDifference(100))
print(time.time()-t0)
