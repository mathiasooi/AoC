from itertools import *
from collections import *
from functools import *
import sys
import re


inp = sys.argv[1] + ".txt"
print(inp)
steps = [(i.split()[0], [int(j) for j in re.findall(r"-?\d+", i)]) for i in open(inp)]

# Part 1 solution
# Very efficient!
# def getcubes(x0, x1, y0, y1, z0, z1):
#     x0 = max(x0, -50)
#     y0 = max(y0, -50)
#     z0 = max(z0, -50)
#     x1 = min(x1, 50)
#     y1 = min(y1, 50)
#     z1 = min(z1, 50)
#     return set(product(range(x0, x1 + 1), range(y0, y1 + 1), range(z0, z1 + 1)))

# on = set()
# for op, bounds in steps:
#     if op == "on":
#         on = on.union(getcubes(*bounds))
#     else:
#         on = on.difference(getcubes(*bounds))
# print(len(on))

def intersection(a, b):
    ax0, ax1, ay0, ay1, az0, az1 = a
    bx0, bx1, by0, by1, bz0, bz1 = b
    if ax0 > bx1 or ax1 < bx0 or ay0 > by1 or ay1 < by0 or az0 > bz1 or az1 < bz0: return (a,)

    cx0, cx1, cy0, cy1, cz0, cz1 = max(ax0, bx0), min(ax1, bx1), max(ay0, by0), min(ay1, by1), max(az0, bz0), min(az1, bz1)
    new = []
    # SO MANY fence post errors :(
    if az0 <= cz0 - 1: new.append((ax0, ax1, ay0, ay1, az0, cz0 - 1))
    if cz1 + 1 <= az1: new.append((ax0, ax1, ay0, ay1, cz1 + 1, az1))
    if ay0 <= cy0 - 1: new.append((cx0, cx1, ay0, cy0 - 1, cz0, cz1))
    if cy1 + 1 <= ay1: new.append((cx0, cx1, cy1 + 1, ay1, cz0, cz1))
    if ax0 <= cx0 - 1: new.append((ax0, cx0 - 1, ay0, ay1, cz0, cz1))
    if cx1 + 1 <= ax1: new.append((cx1 + 1, ax1, ay0, ay1, cz0, cz1))
    return new
    
on = []
for op, bounds in steps:
    new = []
    for x in on:
        new.extend(intersection(x, bounds))
    if op == "on":
        new.append(bounds)
    on = new
total = 0
for x0, x1, y0, y1, z0, z1 in on:
    total += (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)
print(total)

        
