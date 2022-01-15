from itertools import *
from collections import *
import sys
import re
import ast
from functools import reduce

inp = sys.argv[1] + ".txt"
print(inp)
s = [ast.literal_eval(i) for i in open(inp)]

def split(sf):
    if isinstance(sf, int):
        if sf >= 10:
            return (sf // 2, sf - sf // 2), True
    else:
        l, r = sf
        l, t = split(l)
        if not t:
            r, t = split(r)
        if t:
            return (l, r), True
    return sf, False

def addl(sf, x):
    if isinstance(sf, int):
        return sf + x
    return addl(sf[0], x), sf[1]
def addr(sf, x):
    if isinstance(sf, int):
        return sf + x
    return sf[0], addr(sf[1], x)

def explode(sf, d=0):
    if not isinstance(sf, int):
        l, r = sf
        if d >= 4:
            return 0, True, l, r
        else:
            l, t, ll, rr = explode(l, d + 1)
            if t:
                if rr:
                    r = addl(r, rr)
                    rr = 0
            else:
                r, t, ll, rr = explode(r, d + 1)
                if t:
                    if ll:
                        l = addr(l, ll)
                        ll = 0
            if t:
                return (l, r), True, ll, rr
    return sf, False, 0, 0

def magnitude(sf):
    if isinstance(sf, int): return sf
    return 3 * magnitude(sf[0]) + 2 * magnitude(sf[1])

def reduce_(sf):
    t = True
    while t:
        sf, t, _, _ = explode(sf)
        if not t:
            sf, t = split(sf)
    return sf

sfs = [reduce_(i) for i in s]
print(magnitude(reduce(lambda x, y: reduce_((x, y)), sfs)))
print(max(magnitude(reduce_((a, b))) for a, b in product(sfs, repeat=2)))
