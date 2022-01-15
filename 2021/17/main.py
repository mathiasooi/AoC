from itertools import *
from collections import *
import sys
import re

inp = sys.argv[1] + ".txt"
print(inp)
s = open(inp).read()
xs, xe, ys, ye = [int(i) for i in re.findall(r"-?\d+", s)]
print(xs, xe, ys, ye)
def inTarget(x, y) :
   return x >= xs and x <= xe and y >= ys and y <= ye
def simulate():
    my = 0
    total = 0
    i = 0
    for vxx in range(0, xe+1):
        for vy in range(ys, -1 * ys):
            vx = vxx
            x = y = 0
            currmy = 0
            while True:
                i += 1
                x += vx
                y += vy
                vy -= 1
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                currmy = max(currmy, y)

                if x > xe: break
                if y < ys and vy < 0: break

                if inTarget(x, y):
                    total += 1
                    my = max(currmy, my)
                    break
    print(my)
    print(total)
    print(i)
                

simulate()
