#!/usr/bin/env python3
import re

def readNames(filename):
    names = []
    with open(filename,"r") as file:
        for line in file:
            s = re.split('\W+',line)
            s = s[1:-1]
            names.extend(sorted(s))
    return names

def findScores(names):
    ls = [[ord(c) - 64 for c in string] for string in names]
    total = 0
    for i in range(len(ls)):
        score = sum(ls[i])*(i+1)
        total += score
    return total

print(findScores(readNames("p22_names.txt")))
