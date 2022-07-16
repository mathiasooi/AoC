from imports import *

x = [int(i) for i in open("input1")]
y = sum([i//3 - 2 for i in x])
def fuel(i):
    total = 0
    while i > 0:
        i = i//3 - 2
        if (i > 0):
            total += i
    return total
print(sum([fuel(i) for i in x]))