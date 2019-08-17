#!/usr/bin/env python3
import time

# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this
# product?

def adjacentDigitsProduct():
    digits = []

    with open("p8_digits.txt","r") as file:
        for line in file:
            digits.extend([int(x) for x in line if x.isdigit()])

    products = [1 for i in range(len(digits)-13)]
    idx_max = 0

    for i in range(len(digits)-13):
        for j in digits[i:i+13]:
            products[i] *= j
        if products[i] >= products[idx_max]:
            idx_max = i
    return products[idx_max]


t0 = time.time()
print(adjacentDigitsProduct())
print(time.time()-t0)
