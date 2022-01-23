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

players, marbles = [int(i) for i in re.findall(r"\d+", open("input9").read())]
# players, marbles = 9, 25
marbles *= 100
scores = [0]*players

board = [0, 1]
curr = 1
for i in range(2, marbles + 1):
    if not i % 1000000: # uh oh my code takes forever to run ._.
        # maybe should use some linked list or deque thingy. oops!
        # LOL took more than an hour to run
        print(i)
    if i % 23:
        curr = (curr + 1) % len(board) + 1
        board.insert(curr, i)
    else:
        scores[i % players] += i
        curr = (curr - 8) % len(board) + 1
        scores[i % players] += board.pop(curr)
print(max(scores))