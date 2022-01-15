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

s = [list(i.strip()) for i in open("input18")]

dim = 50

def step(grid):
    new = [[0 for _ in range(dim)] for _ in range(dim)]
    for i, j in product(range(dim), repeat=2):
        d = defaultdict(int)
        for dx, dy in product(range(-1, 2), repeat=2):
            if dx == 0 and dy == 0: continue
            if 0 <= i + dx < dim and 0 <= j + dy < dim: 
                d[grid[i + dx][j + dy]] += 1
        if grid[i][j] == ".": new[i][j] = "|" if d["|"] >= 3 else "."
        if grid[i][j] == "|": new[i][j] = "#" if d["#"] >= 3 else "|"
        if grid[i][j] == "#": new[i][j] = "#" if d["#"] >= 1 and d["|"] >= 1 else "."
    return new

# for _ in range(10):
#     # for i in s:
#     #     print(i)
#     s = step(s)
#     # print("AA")

# memo = []
# for i in range(1000000000):
#     memo.append(s)
#     s = step(s)
#     if s in memo:
#         print(i)
#         print(memo.index(s))
#         break

for _ in range(465 + 1000000000 % (493 - 465) - 465 % (493 - 465)):
    s = step(s)
x = sum(sum(i == "|" for i in j) for j in s)
y = sum(sum(i == "#" for i in j) for j in s)
print(x, y, x*y)