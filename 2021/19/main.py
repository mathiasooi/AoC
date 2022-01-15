from itertools import *
from collections import *
import sys
import re

inp = sys.argv[1] + ".txt"
print(inp)
s = [i.split()[4:] for i in open(inp).read().split("\n\n")]
beacons = []
for scanner in s:
    t = []
    for beacon in scanner:
        x, y, z = [int(i) for i in beacon.split(",")]
        t.append((x, y, z))
    beacons.append(t)

def genRot():
    return (i for i in product(permutations(range(3)), product([-1, 1], repeat=3)))
def orient(p, rot):
    return [p[rot[0][i]] * rot[1][i] for i in range(3)]
def offset(p1, p2):
    return tuple(p1[i] - p2[i] for i in range(3))
def add(p1, p2):
    return tuple(p1[i] + p2[i] for i in range(3))
def offsets(b1, b2, r):
    d = defaultdict(int)
    for (p1, p2) in product(b1, b2):
        # d[offset(p1, p2)] += 1
        d[offset(p1, orient(p2, r))] += 1
    for k, v in d.items():
        if v >= 12:
            return k

known = set(beacons.pop(0))
sc = []
while beacons:
    curr = beacons.pop(0)
    t = False
    for r in genRot():
        off = offsets(known, curr, r)
        if off:
            print(off, r)
            sc.append(off)
            known.update(add(orient(p, r), off) for p in curr)
            t = True
            break
            # for p in curr:
            #     p = add(orient(p, r), off)
            #     if p in known:
            #         print(p)
    if t: continue
    beacons.append(curr)
print(len(known))
def mdist(p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(3))
print(max(mdist(p1, p2) for (p1, p2) in product(sc, repeat=2)))
