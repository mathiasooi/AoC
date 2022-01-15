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

s = [int(i) for i in open("input8").read().split()]

def parse(x):
    cc, mdata = x[:2]
    x = x[2:]

    total = 0
    
    for _ in range(cc):
        subtotal, x = parse(x)
        total += subtotal
    total += sum(x[:mdata])
    return total, x[mdata:]

print(parse(s))

def parse2(x):
    cc, mdata = x.pop(0), x.pop(0)
    d = [parse2(x) for _ in range(cc)]
    data = [x.pop(0) for _ in range(mdata)]
    if cc:
        total = 0
        for i in data:
            if (i - 1) in range(cc):
                total += d[i - 1]
    else:
        total = sum(data)
    return total
print(parse2(s))




