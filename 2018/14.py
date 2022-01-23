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

s = "880751"
scores = list("37")
e1, e2 = 0, 1
# while len(scores) - 10 < int(s):
#     for i in str(int(scores[e1]) + int(scores[e2])):
#         scores.append(i)
#     e1 = (e1 + int(scores[e1]) + 1) % len(scores)
#     e2 = (e2 + int(scores[e2]) + 1) % len(scores)
# print("".join(scores[int(s):int(s)+10]))

while s not in "".join(scores[-7:]):  # Can add multiple scores in one iteration
    for i in str(int(scores[e1]) + int(scores[e2])):
        scores.append(i)
    e1 = (e1 + int(scores[e1]) + 1) % len(scores)
    e2 = (e2 + int(scores[e2]) + 1) % len(scores)
print(len(scores) - 7)