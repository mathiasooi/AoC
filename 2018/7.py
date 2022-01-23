from itertools import *
from collections import *
from functools import *
from math import *
from operator import *
from string import *
from copy import deepcopy
from heapq import heapify, heappush, heappop
import numpy as np
import ast
import sys
import os
import re

s = [i.split() for i in open("input7")]
conditions = defaultdict(list)
nodes = set()
for _, a, _, _, _, _, _, b, _, _ in s:
    conditions[b].append(a)
    nodes.add(a)
    nodes.add(b)
nodes = sorted(nodes)
print(nodes)
print(conditions)

# def dfs(curr, v):
#     v.append(curr)
#     for next in nodes:
#         if next not in v and all(i in v for i in conditions[next]):
#             dfs(next, v)
#     return v

# for c in nodes:
#     if conditions[c]: continue
#     x = dfs(c, [])
#     print(c, x, conditions[c])
#     if len(x) == len(nodes):
#         print(c, "".join(x))

slaves, t = 5, 0
m = {k: v for (k, v) in zip(ascii_uppercase, range(1, 27))}
labor = []
finished = set()
def findJob():
    for c in nodes:
        if all(i in finished for i in conditions[c]):
            return c

while nodes or labor:
    while labor and labor[0][0] == t:
        finished.add(heappop(labor)[1])
        slaves += 1
    if slaves:
        while slaves and (job := findJob()):
            heappush(labor, (t + m[job] + 60, job))
            nodes.remove(job)
            slaves -= 1
    print(t, labor, finished)
    if labor: t += labor[0][0] - t
print(t)
