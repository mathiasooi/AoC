from itertools import *
from collections import *
import sys
import re

inp = sys.argv[1] + ".txt"
print(inp)
algo, image = open(inp).read().split("\n\n")
algo = [i == "#" for i in algo]
# print(algo[0], algo[-1]) # wtf test example didnt have this actual scam
image = set((i, j) for i, line in enumerate(image.split()) for j, x in enumerate(line) if x == "#")

def step(image, t):
    new = set()
    x0, x1 = min(image, key = lambda x: x[0])[0], max(image, key = lambda x: x[0])[0]
    y0, y1 = min(image, key = lambda x: x[1])[1], max(image, key = lambda x: x[1])[1]
    # print(x0, x1, y0, y1)
    for i in range(x0 - 1, x1 + 2):
        for j in range(y0 - 1, y1 + 2):
            s = ""
            for dx, dy in product(range(-1, 2), range(-1, 2)):
                nx, ny = i+dx, j+dy
                if x0 <= nx <= x1 and y0 <= ny <= y1:
                    s += "01"[(nx, ny) in image]
                else:
                    s += t
            if algo[int(s, 2)]:
                new.add((i, j))
    return new


for i in range(2):
    image = step(image, str(i % 2))
print(len(image))

for i in range(48):
    image = step(image, str(i % 2))
print(len(image))
