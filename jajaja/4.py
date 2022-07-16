from imports import *

a = 264360
b = 746325
def valid(x):
    t = False
    for i, j in zip(str(x), str(x)[1:]):
        if i == j: t = True
        if int(i) > int(j): return False
    return t
def valid2(x):
    t = False
    for i, j in zip(x, x[1:]):
        if i == j and x.count(i) == 2: t = True
        if int(i) > int(j): return False
    return t
print(sum(valid(i) for i in range(a, b+1)))
print(sum(valid2(str(i)) for i in range(a, b+1)))
