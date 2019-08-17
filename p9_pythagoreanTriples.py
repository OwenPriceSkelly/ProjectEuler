#!/usr/bin/env python3

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# i.e. find a triple that sums to n, and return the product

def pythagoreanTriple(n):
    triples = []
    # generate pythagorean triples:
    for c in range(n):
        for b in range(c):
            for a in range (b):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    print([a,b,c])
                    return
    return

pythagoreanTriple(1000)
