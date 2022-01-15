s = [i.strip() for i in open("input.txt").read().split()]
from collections import defaultdict
from itertools import filterfalse
d = defaultdict(int)
for i in s:
    for j in range(len(i)):
        d[j] += int(i[j])
x = ""
for i in d:
    if d[i] > len(s) // 2:
        x += "1"
    else:
        x += "0"

y = "".join("1" if i == "0" else "0" for i in x)
print(int(x, 2)*int(y, 2))

x = s[:]
z = 0
while len(x) > 1:
    y = sum(int(i[z]) for i in x)
    if y >= len(x) - y:
        x[:] = filterfalse(lambda x: x[z] == "0", x)
    else:
        x[:] = filterfalse(lambda x: x[z] == "1", x)
    z += 1
a = x[0]

x = s[:]
z = 0
while len(x) > 1:
    y = sum(int(i[z]) for i in x)
    if y < len(x) - y:
        x[:] = filterfalse(lambda x: x[z] == "0", x)
    else:
        x[:] = filterfalse(lambda x: x[z] == "1", x)
    z += 1
b = x[0]
print(int(a, 2) * int(b, 2))