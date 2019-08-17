#!/usr/bin/env python3
from time import time

def readFile(filename):
    with open(filename,"r") as file:
        triangles = [[int(n) for n in line.split()] for line in file]
    return triangles[::-1]

def maxTotal(triangles):
    for line in triangles: print(line)
    for i in range(1,len(triangles)):
        for j in range(len(triangles[i])):
            triangles[i][j] = triangles[i][j] + max(triangles[i-1][j],triangles[i-1][j+1])
    for line in triangles: print(line)
    return

t0 = time()
maxTotal(readFile("p18_triangle.txt"))
print(time()-t0)
