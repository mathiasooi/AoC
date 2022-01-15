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

s = open("input5").read().strip()


def willReact(a, b):
    return abs(ord(a) - ord(b)) == 32
def solve(x):
    l = []
    for i in x:
        if l and willReact(l[-1], i):
            l.pop()
        else:
            l.append(i)
    return l
# print(len(solve(s)))
print(min(len(solve(s.replace(i, "").replace(i.upper(), ""))) for i in ascii_lowercase))