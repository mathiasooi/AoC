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

initial, *pairs = re.findall(r"[.#]+", open("input12").read())
m = defaultdict(bool, {k: v == "#" for (k, v) in zip(*[iter(pairs)]*2)})
pots = defaultdict(bool, {i: v == "#" for (i, v) in enumerate(initial)})

seen = []
for j in range(1000):
    seen.append("".join(".#"[v] for v in pots.values()).strip("."))
    new = defaultdict(bool)
    for i in range(min(pots) - 5, max(pots) + 5):
        new[i] = m["".join(".#"[pots[i+j]] for j in range(-2, 3))]
    pots = new
    pt = "".join(".#"[v] for v in pots.values()).strip(".")
    if pt in seen:
        # print(pt)
        # print(seen.index(pt))
        # print([i for i in pots if pots[i]])
        print(sum((50000000000 - j + k - 1)*v for (k, v) in pots.items()))
        break

    if j == 19:
        print(sum(k*v for (k, v) in pots.items()))
