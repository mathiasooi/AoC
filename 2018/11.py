from itertools import *
from collections import *
from functools import *
from math import *
from msilib.schema import TypeLib
from operator import *
from string import *
from copy import deepcopy
from heapq import heappush, heappop
import numpy as np
import ast
import sys
import os
import re

# gsn = 42
gsn = 9005
# bruh this looks like 2d prefix sujms askdopakspdokashduiahsduiashdiuhaIOADJGFI

def power(x, y):
    if min(x, y) == 0: return 0
    rackid = x + 10
    p = rackid * y
    p += gsn
    p *= rackid
    p = p // 100 % 10
    return p - 5


grid = [[power(i, j) for i in range(301)] for j in range(301)]
for i in range(1, 301):
    for j in range(1, 301):
        grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1] + grid[i][j]

# bestv = 0
# tl = (0, 0)
# for i in range(1, 301 - 3):
#     for j in range(1, 301 - 3):
#         v = grid[i+3][j+3] - grid[i][j+3] - grid[i+3][j] + grid[i][j]
#         if v > bestv:
#             bestv = v
#             tl = (i+1, j+1)
# print(bestv, tl)

bestv = 0
tl = (0, 0, 0)
for size in range(1, 300):
    for i in range(301 - size):
        for j in range(301 - size):
            v = grid[i+size][j+size] - grid[i][j+size] - grid[i+size][j] + grid[i][j]
            if v > bestv:
                bestv = v
                tl = (j+1, i+1, size)
print(bestv, tl)

