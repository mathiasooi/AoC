from imports import *

code = [int(i) for i in open("input5").read().split(",")]
ip = 0
inpx = 5
def add(cc, a, b, c): cc[c] = cc[a] + cc[b]
def mul(cc, a, b, c): cc[c] = cc[a] * cc[b]
def inp(cc, a): cc[a] = inpx
def out(cc, a): print(cc[a], end="")
def pos(cc, a): return cc[a]
def imm(cc, a): return a
def jt(cc, a, b): 
    global ip
    if cc[a]: ip = cc[b]
def jf(cc, a, b):
    global ip
    if not cc[a]: ip = cc[b]
def lt(cc, a, b, c): cc[c] = int(cc[a] < cc[b])
def eq(cc, a, b, c): cc[c] = int(cc[a] == cc[b])
def halt(*args): exit()
getop = {
    1: (add, 3),
    2: (mul, 3),
    3: (inp, 1),
    4: (out, 1),
    5: (jt, 2),
    6: (jf, 2),
    7: (lt, 3),
    8: (eq, 3),
    99: (halt, 0)
}
getmode = {
    "0": pos,
    "1": imm
}
def step():
    global ip
    # print("IP: ", ip)
    # print(code)
    rmode, op = divmod(code[ip], 100)
    # print("OP:", op)
    ip += 1
    rmode = str(rmode).zfill(3)[::-1]
    f, inc = getop[op]
    # print(f, inc, rmode[:inc])
    # print(list(zip(rmode[:inc], range(ip, ip+3))))
    params = [getmode[c](code, p) for c,p in zip(rmode[:inc], range(ip, ip+3))]
    # print(params)
    ip += inc
    f(code, *params)

for i in range(100000):
    # print(i)
    step()

