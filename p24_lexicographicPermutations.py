#!/usr/bin/env python3
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
def memoize(f):
    cache = {}
    def mem(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return mem

@memoize
def factorial(n):
    if n < 2: return 1
    return n*factorial(n-1)

def nth_lex(n,digits,ans):
    d = factorial(len(digits)-1)
    idx = n//d
    n = n%d
    if n == 1:
        ans.extend(digits)
        return ans
    elif n == 0:
        # if idx != 0:
        ans.append(digits.pop(idx-1))
        ans.extend(digits[::-1])
        return ans

    ans.append(digits.pop(idx))
    return nth_lex(n,digits,ans)

digs = [0,1,2]
for i in range(factorial(len(digs))):
    ans = []
    print(nth_lex(i,digs,ans))
