from imports import *

d = defaultdict(list)
dd = defaultdict(list)
for a, b in [i.strip().split(")") for i in  open("input6")]:
    d[a].append(b)
    d[b]
    dd[a].append(b)
    dd[b].append(a)

def foo(x):
    return len(d[x]) + sum(foo(next) for next in d[x])

print(sum(foo(x) for x in d))

v = set()
dist = {"SAN": 0}
q = ["SAN"]
v.add("SAN")
while q:
    c = q.pop(0)
    print(c, dd[c])
    for n in dd[c]:
        if n in v: continue
        q.append(n)
        v.add(n)
        dist[n] = dist[c] + 1
print(dist["YOU"]-2)