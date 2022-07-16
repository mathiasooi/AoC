from imports import *


m1, m2 = [i.split(",") for i in open("input3").readlines()]
print(m1, m2)
def foo(moves):
    v = set()
    dd = defaultdict(lambda : 1000000000)
    x = y = 0
    # v.add((x, y))
    i = 0
    for move in moves:
        d = move[0]
        dx = dy = 0
        if (d == "L"): dx = -1
        if (d == "R"): dx = 1
        if (d == "U"): dy = 1
        if (d == "D"): dy = -1
        for _ in range(int(move[1:])):
            i += 1
            x += dx
            y += dy
            v.add((x, y))
            dd[(x, y)] = min(dd[(x, y)], i)
            # if (x, y) in v:
            #     intersect.add((x, y))
    return v, dd
print(min(abs(i)+abs(j) for i,j in foo(m1)[0].intersection(foo(m2)[0])))
a, b = foo(m1)
c, d = foo(m2)
print(min(b[i] + d[i] for i in a.intersection(c)))