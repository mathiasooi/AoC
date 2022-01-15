from itertools import *
from collections import *
import sys
import re
import matplotlib.pyplot as plt

inp = sys.argv[1] + ".txt"
print(inp)
s = open(inp).read().split("\n\n")
points = set()
folds = []
for x, y in [i.split(",") for i in s[0].split()]:
    points.add((int(x), int(y)))
for i in s[1].split("\n"):
    i = i.split("=")
    fold = (i[0][-1], int(i[1]))
    folds.append(fold)

def reflect(p, line):
    pp = set()
    if line[0] == "y":
        for x, y in p:
            if y <= line[1]: pp.add((x, y))
            else: pp.add((x, 2*line[1]-y))
    else:
        for x, y in p:
            if x <= line[1]: pp.add((x, y))
            else: pp.add((2*line[1]-x, y))
    return pp

print(len(reflect(points, folds[0])))
for fold in folds:
    print(fold)
    points = reflect(points, fold)
print(points)
xs, ys = zip(*points)
plt.figure(figsize=(20, 40))
plt.ylim(max(ys), min(ys))
plt.plot(xs, ys, "rp", markersize=20)
plt.show()