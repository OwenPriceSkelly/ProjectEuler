#!/usr/bin/env python3
# what d < 1000 contains the longest recurring decimal cycle for 1/d?


def primesBelow(n):
    # sieve up to root n

    N =  [x for x in range(2,n)]
    primes = []
    while N:
        primes.append(N[0])
        for i in range(len(N)):
            if N[i] % primes[-1] == 0:
                N[i] = 0

        N = [x for x in N if x != 0]

        if N[0]**2 > n:
            primes.extend(N)
            break
    # print(primes)
    return primes

def lenCycle(p):
    c = 0
    n = 1
    while True:
        c += 1
        n = 10*n % p
        if n == 1 : break
    return c

primes = primesBelow(10)
primes = [p for p in primes if p > 5]
cycles = [lenCycle(p) for p in primes]
print("{} has a {}- cycle".format(primes[cycles.index(max(cycles))],max(cycles)))
