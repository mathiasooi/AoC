from itertools import *
from collections import *
from functools import *
import sys
import re


inp = sys.argv[1] + ".txt"
print(inp)
_, pp1, _, pp2 = [int(i) for i in re.findall(r"\d", open(inp).read())]
# p1, p2 = 4, 8
# p1, p2 = 9-1, 4-1
p1, p2 = pp1 - 1, pp2 - 1

def roll():
    x = 1
    while True:
        yield x
        x = (x % 100) + 1
    
i = score1 = score2 = 0
dice = roll()
while True:
    rolled = next(dice) + next(dice) + next(dice)
    p1 = (p1 + rolled) % 10
    score1 += p1+1
    i += 3
    if score1 >= 1000: break

    rolled = next(dice) + next(dice) + next(dice)
    p2 = (p2 + rolled) % 10
    score2 += p2+1
    i += 3
    if score2 >= 1000: break
print(min(score1, score2) * i)

# p1, p2 = 4, 8
# p1, p2 = 9-1, 4-1
p1, p2 = pp1 - 1, pp2 - 1

@cache  # DP, not cheating btw :D
def solve(p1, p2, score1, score2):
    if max(score1, score2) >= 21:
        return score1 >= 21, score2 >= 21
    r1 = r2 = 0
    for d1, d2, d3 in product(range(1, 4), repeat=3):
        p = p1 + d1 + d2 + d3
        p %= 10
        a, b = solve(p2, p, score2, score1 + p + 1)
        r1 += b
        r2 += a
    return (r1, r2)
print(max(solve(p1, p2, 0, 0)))