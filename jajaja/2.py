from imports import *

code = [int(i) for i in open("input2").read().split(",")]

getop = {1: add, 2:mul, 99:99}

cc = deepcopy(code)
def foo(cc):
    for i in range(0, len(cc), 4):
        op = getop[cc[i]]
        if op == 99: 
            return cc[0]
        else:
            cc[cc[i+3]] = op(cc[cc[i+1]], cc[cc[i+2]])
print(foo(cc))


for i in range(100):
    for j in range(100):
        cc = deepcopy(code)
        cc[1], cc[2] = i, j
        if foo(cc) == 19690720:
            print(100*i*j)
