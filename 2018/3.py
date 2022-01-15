from itertools import *
from collections import *
from functools import *
from math import *
from operator import *
from string import *
from copy import deepcopy
from heapq import heappush, heappop
import numpy as np
import ast
import sys
import os
import re

s = [[int(i) for i in re.findall("-?\d+", j)] for j in open("input3")]

d = defaultdict(int)
for rid, x, y, lx, ly in s:
    for i in range(x, x + lx):
        for j in range(y, y + ly):
            d[(i, j)] += 1
print(sum(i >= 2 for i in d.values()))

def nooverlap(x, y, lx, ly):
    for i in range(x, x + lx):
        for j in range(y, y + ly):
            if d[(i, j)] != 1: return False
    return True

for i in s:
    if nooverlap(*i[1:]): print(i[0])