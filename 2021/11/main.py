from itertools import *
from collections import *
import sys
import re

s = [[int(i) for i in j] for j in open("input.txt").read().split()]
def step():
    for i in range(len(s)):
        for j in range(len(s[0])):
            s[i][j] += 1
    flashed = []
    while any(s[i][j] > 9 for i in range(len(s)) for j in range(len(s[0]))):
        flashed += flash()
        for (x, y) in flashed:
            s[x][y] = 0

    for i in range(len(s)):
        print(s[i])
    print()
    return len(flashed)
def flash():
    d = defaultdict(int)
    flashed = []

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] <= 9: continue
            flashed.append((i, j))
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    nx, ny = i + di, j + dj
                    if nx >= 0 and nx < len(s) and ny >= 0 and ny < len(s[0]):
                        d[(nx, ny)] += 1
    for ((x, y), v) in d.items():
        s[x][y] += v
    return flashed
    
# Part 1
# x = 0
# for _ in range(100):
#     x += step()
# print(x)

x = 0
i = 0
while x != len(s) * len(s[0]):
    x = step()
    i += 1
print(i)
