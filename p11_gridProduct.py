#!/usr/bin/env python3
from functools import reduce

def product(list): return reduce(lambda x,y: x*y,list)

# find the largest product of n adjacent numbers in a grid
def adjacentGridProduct(n,filename):
    grid = []
    with open(filename,"r") as file:
        for line in file:
            grid.append([int(x) for x in line.split()])
    max_prod,row,col = 0,0,0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Vertical product
            if row + n <= len(grid):
                prod = product([ grid[row + i][col] for i in range(0,n)])
                if prod > max_prod: max_prod = prod

            # Horizontal product
            if col + n <= len(grid[row]):
                prod = product([ grid[row][col + i] for i in range(0,n)])
                if prod > max_prod: max_prod = prod

            # Lower-Diagonal product
            if row + n <= len(grid) and col + n <= len(grid[row]):
                prod = product([ grid[row + i][col + i] for i in range(0,n)])
                if prod > max_prod: max_prod = prod

            # Upper-Diagonal product
            if row - (n-1) >= 0 and col + n <= len(grid[row]):
                prod = product([ grid[row - i][col + i] for i in range(0,n)])
                if prod > max_prod: max_prod = prod

    print(max_prod)
adjacentGridProduct(4,"p11_grid.txt")
