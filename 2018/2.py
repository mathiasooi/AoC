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

s = [i.strip() for i in open("input2")]
twice = thrice = 0
for i in s:
    c = Counter(i)
    twice += 2 in c.values()
    thrice += 3 in c.values()
print(twice * thrice)

def numdiffer(s1, s2):
    return sum(s1[i] == s2[i] for i in range(len(s1)))


for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if numdiffer(s[i], s[j]) == len(s[i])-1:
            for k in range(len(s[i])):
                if s[i][k] == s[j][k]: print(s[i][k], end="")
