from imports import *

x = [int(i) for i in open("input8").read()]
layers = [x[i*150:(i+1)*150] for i in range(len(x)//150)]
# print([Counter(i) for i in layers])
best, bl = 10000000, 0
for i in range(len(layers)):
    if (layers[i].count(0) < best):
        best = layers[i].count(0)
        bl = i
print(layers[bl].count(1)*layers[bl].count(2))

x = layers[0]
for layer in layers[1:]:
    for i in range(150):
        x[i] = layer[i] if x[i] == 2 else x[i]

for i in range(6):
    for j in range(25):
        if x[i*25+j] == 1: print("*", end="")
        else: print(" ", end="")
    print()