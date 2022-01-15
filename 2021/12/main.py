from itertools import *
from collections import *
import sys
import re

inp = sys.argv[1] + ".txt"
s = [i for i in open(inp).read().split()]
adj = defaultdict(list)
for i in s:
    a, b = i.split("-")
    adj[a].append(b)
    adj[b].append(a)


def dfs(curr, v):
    if curr == "end":
        return 1
    if curr.islower() and curr in v:
        return 0
    v = v.copy()
    v.add(curr)
    x = 0
    for next in adj[curr]:
        x += dfs(next, v)
    return x

print(dfs("start", set()))


def dfs2(curr, v, vv=False):
    if curr == "end":
        return 1
    if curr.islower() and curr in v:
        if not vv:
           vv = True
        else:
            return 0
    v = v.copy()
    v.add(curr)
    x = 0
    for next in adj[curr]:
        if next == "start": continue
        x += dfs2(next, v, vv)
    return x
print(dfs2("start", set()))