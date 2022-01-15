from itertools import *
from collections import *
import sys
import re
from math import prod

inp = sys.argv[1] + ".txt"
print(inp)
s = open(inp).read().strip()
conv = {i:j for (i, j) in zip("0123456789ABCDEF", ["".join(p) for p in product("10", repeat=4)][::-1])}
data = "".join(map(lambda x: conv[x], s))

total = 0
def parse(packet):
    v = int(packet[:3], 2)
    t = int(packet[3:6], 2)
    packet = packet[6:]
    global total
    total += v
    if t == 4:
        litv = ""
        for i in range(0, len(packet), 5):
            litv += packet[i+1: i+5]
            if packet[i] == "0":
                packet = packet[i+5:]
                return packet, int(litv, 2)
    else:
        i = int(packet[0], 2)
        packet = packet[1:]
        subvs = []
        if i == 0:
            l = int(packet[:15], 2)
            packet = packet[15:]
            sub = packet[:l]
            while sub:
                sub, vv = parse(sub)
                subvs.append(vv)
            packet = packet[l:]
        else:
            l = int(packet[:11], 2)
            packet = packet[11:]
            for _ in range(l):
                packet, vv = parse(packet)
                subvs.append(vv)
    v = 0
    if t == 0: v = sum(subvs)
    elif t == 1: v = prod(subvs)
    elif t == 2: v = min(subvs)
    elif t == 3: v = max(subvs)
    elif t == 5: v = subvs[0]>subvs[1]
    elif t == 6: v = subvs[0]<subvs[1]
    elif t == 7: v = subvs[0]==subvs[1]
    return packet, v


x = parse(data)
print(total)
print(x[1])
