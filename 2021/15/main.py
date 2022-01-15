from itertools import *
from collections import *
import sys
import re
from heapq import heappop, heappush

inp = sys.argv[1] + ".txt"
print(inp)
g = [[int(i) for i in j] for j in open(inp).read().split()]
def dijkstra(g, p2=False):
    heap = [(0,0,0)]
    v = {(0, 0)}

    if p2:
        gg = [[0 for _ in range(5*len(g))] for _ in range(5*len(g))]
        for i in range(len(gg)):
            for j in range(len(gg)):
                d = i//len(g) + j//(len(g))
                n = g[i%len(g)][j%len(g)]
                gg[i][j] = ((n + d) - 1) % 9 + 1
        g = gg

    while heap:
        d, x, y = heappop(heap)
    
        if (x, y) == (len(g)-1, len(g)-1): 
            return d
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(g) or ny < 0 or ny >= len(g) or (nx, ny) in v: continue
            v.add((nx, ny))
            heappush(heap, (d + g[nx][ny], nx, ny))


print(dijkstra(g))
print(dijkstra(g, p2=True))
