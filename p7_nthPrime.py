#!/usr/bin/env python3
import math
import time
# What is the 10,001st prime number?
def nthPrime(n):
    # to calculate the nth prime number,
    # test number k for divisibility by previous primes up to k^(1/2)
    # if k is composite, increment k and check divisibility for k+1
    # if not, add k to list of primes
    primes = []
    k = 2
    for i in range(n):
        primes.append(k)
        k += 1
        j=0
        while(primes[j]**2 <= k):
            if(k % primes[j] == 0):
                j = 0
                k += 1
            else:
                j += 1
    return primes[n-1]

t0 = time.time()
print(nthPrime(10001))
print(time.time()-t0)
