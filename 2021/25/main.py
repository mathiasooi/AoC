from itertools import *
from collections import *
from functools import *
import sys
import re


inp = sys.argv[1] + ".txt"
s = [list(i) for i in open(inp).read().split()]
col, row = len(s), len(s[0])
right = {(i, j) for (i, j) in product(range(col), range(row)) if s[i][j]== ">"}
down = {(i, j) for (i, j) in product(range(col), range(row)) if s[i][j] == "v"}
prev = right | down

i = 1
while True:
    m = right | down
    right = {(x, y) if (x, (y+ 1) % row) in m else (x, (y+ 1) % row) for (x, y) in right}
    m = right | down
    down = {(x, y) if ((x + 1) % col, y) in m else ((x + 1) % col, y) for (x, y) in down}
    new = right | down
    if new == prev: break
    prev = new
    i += 1
print(i)



