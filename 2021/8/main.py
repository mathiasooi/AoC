from itertools import permutations
s = [i.split(" | ") for i in open("input.txt").readlines()]
x = 0
for _, i in s:
    x += sum(len(k) in [2,3,4,7] for k in i.split())

print(x)
z = 0
for i, j in s:
    for a,b,c,d,e,f,g in permutations("abcdefg"):
        # if "".join((a,b,c,d,e,f,g)) != "deafgbc": continue
        dd = ["".join(sorted(x)) for x in [(a,b,c,e,f,g), (c,f), (a,c,d,e,g), (a,c,d,f,g), (b,c,d,f), (a,b,d,f,g), (a,b,d,e,f,g), (a,c,f), (a,b,c,d,e,f,g), (a,b,c,d,f,g)]]
        # print(d)

        t = any("".join(sorted(x)) not in dd for x in i.split())
        if not t:
            t = any("".join(sorted(y)) not in dd for y in j.split())
        if t: continue
        
        m = 0
        # print(a,b,c,d,e,f,g)
        for n in j.split():
            m *= 10
            m += dd.index("".join(sorted(n)))
        # print(m)
        z += m
        break
print(z)



