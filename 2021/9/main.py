m = [[int(i) for i in s.strip()] for s in open("input.txt")]

c = 0
for x in range(len(m)):
    for y in range(len(m[0])):
        t = True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(m) or ny < 0 or ny >= len(m[0]): continue
            if m[nx][ny] <= m[x][y]:
                t = False
                break
        if t:
            c += m[x][y] + 1
print(c)

v = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] == 9: v[x][y] = True
def dfs(cx, cy, t):
    v[cx][cy] = True
    t += 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx >= len(m) or ny < 0 or ny >= len(m[0]): continue
        if not v[nx][ny]:
            t = dfs(nx, ny, t)
    return t
l = []
for x in range(len(m)):
    for y in range(len(m[0])):
        if not v[x][y]:
            l.append(dfs(x, y, 0))
l.sort()      
print(l[-1] * l[-2] * l[-3])