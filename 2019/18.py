from imports import *

g = [list(l.strip()) for l in open("input18")]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == "@": sx, sy = i, j
totalkeys = 26
print(sx, sy)

q = deque(((sx,sy,set(),0),)) # (x, y, past keys, steps)
v = set()
while q:
    c = q.popleft()
    t = (c[0], c[1], frozenset(c[2])) 
    if t in v: continue
    v.add(t)
    # print(c)
    nk = c[2].copy()
    if g[c[0]][c[1]].islower(): nk.add(g[c[0]][c[1]])
    if (len(nk) == totalkeys):
        print(c[3]+1)
        exit()
    # if g[c[0]][c[1]].isupper() and g[c[0]][c[1]].lower() not in nk: continue
    for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        nx = c[0] + dx
        ny = c[1] + dy
        if g[nx][ny] == "#": continue  # grid bounded by "#"
        if g[nx][ny].isupper() and g[nx][ny].lower() not in nk: continue
        q.append((nx, ny, nk, c[3]+1))
