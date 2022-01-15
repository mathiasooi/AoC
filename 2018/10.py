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
import matplotlib.pyplot as plt

s = [[int(j) for j in re.findall(r"-?\d+", i)] for i in open("input10")]
print(s)

# def containWord(xs, ys):
#     return sum(i > 5 for i in Counter(xs).values()) > 2 or sum(i > 5 for i in Counter(ys).values()) > 2

def bboxSize(xs, ys):
    return abs(min(xs) - max(xs)) * abs(min(ys) - max(ys))

t = min((bboxSize([x + t * vx for x, _, vx, _ in s], [y + t * vy for _, y, _, vy in s]), t) for t in range(1000000))
# t = 10888
xs = [x + t * vx for x, _, vx, _ in s]
ys = [y + t * vy for _, y, _, vy in s]
# print(t)
plt.scatter(xs, ys)  # look at it upside down or reverse the axis
plt.show()