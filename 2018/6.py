from itertools import *
from collections import *
from functools import *
from math import *
from operator import *
from string import *
from copy import deepcopy
from heapq import heappush, heappop
import ast
import sys
import os
import re

points = [tuple(map(int, j.split(", "))) for j in open("input6")]
def nearest(x, y):
    best, besti = 10000, None
    for (i, (px, py)) in enumerate(points):
        dist = abs(x - px) + abs(y - py)
        if dist < best:
            best, besti = dist, i
        elif dist == best:
            besti = None
    return besti

def areas(n):
    d = [0]*len(points)
    for x, y in product(range(-n, n), repeat=2):
        i = nearest(x, y)
        if i is not None:
            d[i] += 1
    return set(d)

print(max(areas(1000).intersection(areas(1001))))


total = 0
for x, y in product(range(-1000, 1000), repeat=2):
    sumdist = 0
    for px, py in points:
        sumdist += abs(x - px) + abs(y - py)
    if sumdist < 10000:
        total += 1
print(total)
