from imports import *


sig = [int(i) for i in open("input16").read()]
cyc = [0, 1, 0, -1]

for _ in range(100):
    t = []
    for i in range(len(sig)):
        total = 0
        for j in range(len(sig)):
            x = sig[j] * cyc[((j+1)//(i+1))%4]
            # print(x, end=" ")
            total += x
        t.append(abs(total)%10)
        # print()
    sig = t
        

print(sig[:8])
# i just remembered the problem name is FFT...nuuuuuuuuuuuuuu