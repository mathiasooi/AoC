from imports import *

moons = [[int(i) for i in re.findall(r"-?\d+", i)] + [0,0,0] for i in open("input12")]

def step():
    for i, m1 in enumerate(moons):
        for m2 in moons[i+1:]:
            for j in range(3):
                if m1[j] < m2[j]:
                    m1[j+3] += 1
                    m2[j+3] -= 1
                elif m1[j] > m2[j]:
                    m1[j+3] -= 1
                    m2[j+3] += 1
    for m in moons:
        for j in range(3):
            m[j] += m[j+3]

# total = 0
# for m in moons:
#     total += sum(abs(i) for i in m[:3]) * sum(abs(i) for i in m[3:])

# print(total)

xs, xi = set(), 0
ys, yi = set(), 0
zs, zi = set(), 0

for i in range(1000000):
    step()
    if not xi:
        k = tuple([(m[0], m[3]) for m in moons])
        if k in xs: xi = i
        xs.add(k)
    if not yi:
        k = tuple([(m[1], m[4]) for m in moons])
        if k in ys: yi = i
        ys.add(k)
    if not zi:
        k = tuple([(m[2], m[5]) for m in moons])
        if k in zs: zi = i
        zs.add(k)

print(lcm(lcm(xi, yi), zi))