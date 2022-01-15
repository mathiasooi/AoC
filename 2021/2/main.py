s = [x.split() for x in open("input.txt").read().split("\n")]
x = y = 0
for d, i in s:
    i = int(i)
    if d == "down":
        y += i
    if d == "up":
        y -= i
    if d == "forward":
        x += i
print(x * y)

x = y = a = 0
for d, i in s:
    i = int(i)
    if d == "down":
        a -= i
    if d == "up":
        a += i
    if d == "forward":
        x += int(i)
        y += a * int(i)
print(x * y)