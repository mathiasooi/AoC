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

s = sorted([i.strip() for i in open("input4")])
guards = defaultdict(Counter)
start = guard = 0
for i in s:
    x = int(re.findall(r"\d+", i)[-1])
    if "Guard" in i:
        guard = x
    elif "falls" in i:
        start = x
    elif "wakes" in i:
        guards[guard].update(range(start, x))
a = max(guards, key=lambda x: sum(guards[x].values()))
b = guards[a].most_common(1)[0][0]
print(a * b)
a = max(guards, key=lambda x: guards[x].most_common(1)[0][1])
b = guards[a].most_common(1)[0][0]
print(a * b)
