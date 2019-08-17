#!/usr/bin/env python3
# Find the sum of all the primes below two million.

def sumOfPrimesBelow(n):

    # sieve up to root n
    N = [x for x in range(2,n)]
    primes = []
    while N:
        primes.append(N[0])
        for i in range(len(N)):
            if N[i] % primes[-1] == 0:
                N[i] = 0
        N = [x for x in N if x !=0]
        if N[0]**2 > n:
            primes.extend(N)
            break
    # print(primes)
    return sum(primes)

print(sumOfPrimesBelow(2000000))
