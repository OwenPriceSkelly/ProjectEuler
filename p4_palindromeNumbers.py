#!/usr/bin/env python3
import math
import time
# problem 4
# Find the largest palindrome made from the product of two
# 3-digit numbers
def isPalindrome(n):
    n = str(n)
    return n == n[::-1]
    
def palindromeNumbers():
    max = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            if isPalindrome(i*j) and i*j>max:
                max = i*j
    return max
