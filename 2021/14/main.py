from itertools import *
from collections import *
import sys
import re

inp = sys.argv[1] + ".txt"
print(inp)

x = open(inp).read().split("\n\n")
poly = x[0]
d = {j: k for (j, k) in [i.split(" -> ") for i in x[1].split("\n")]}

pairs = defaultdict(int)
chars = Counter(poly)
for i in range(len(poly) - 1):
    pairs[poly[i: i+2]] += 1
print(pairs)

def simulate(steps):
    x = pairs.copy()
    y = chars.copy()
    for _ in range(steps):
        newx = defaultdict(int)
        for pair, v in x.items():
            newx[pair[0]+d[pair]] += v
            newx[d[pair]+pair[1]] += v
            y[d[pair]] += v
        x = newx
    return max(y.values()) - min(y.values())

print(simulate(10))
print(simulate(40))
