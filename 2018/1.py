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

s = [int(i) for i in open("input1")]
print(sum(s))
reached = set()
x = 0
for _ in range(1000):
    for i in s:
        reached.add(x)
        x += i
        if x in reached:
            print(x)
            sys.exit()