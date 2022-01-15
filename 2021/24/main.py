from itertools import *
from collections import *
from functools import *
import sys
import re

inp = sys.argv[1] + ".txt"
print(inp)
s = open(inp).read().split("\n")

# Only instructions that differ for every input
xs = [int(re.search(r"-?\d+", i)[0]) for i in s if i.startswith("add x") and i[-1] != "z"]
ys = [int(re.search(r"-?\d+", s[i])[0]) for i in range(15, len(s), 18)]
print(xs)
print(ys)
stack = []
d = {}
for i in range(14):
    if xs[i] > 0:
        stack.append((i, ys[i]))
    else:
        a, b = stack.pop()
        d[i] = (a, b + xs[i])
dd = {}
for i, (j, k) in d.items():
    dd[i] = min(9, 9 + k)
    dd[j] = min(9, 9 - k)
print("".join(str(dd[x]) for x in range(14)))
for i, (j, k) in d.items():
    dd[i] = max(1, 1 + k)
    dd[j] = max(1, 1 - k)
print("".join(str(dd[x]) for x in range(14)))
