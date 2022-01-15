from itertools import *
from collections import *
import sys
import re

s = open("input.txt").read().split()

p = {")": 3, "]": 57, "}": 1197, ">": 25137}
m = {"(": ")", "[": "]", "{": "}", "<": ">"}
x = 0
y = []

for line in s:
    d = []
    t = False
    for c in line:
        if c in m:
            d.append(c)
        else:
            if m[d[-1]] != c:
                x += p[c]
                t = True
                break
            d.pop()
    if not t:
        z = 0
        pp = [0, "(", "[", "{", "<"]
        for c in reversed(d):
            z = z*5 + pp.index(c)
        y.append(z)
        
y.sort()
print(x)
print(y[len(y)//2])