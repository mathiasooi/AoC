from collections import defaultdict
s = [i.split(" -> ") for i in open("input.txt").read().split("\n")]
start = []
end = []
for i, j in s:
    i = [int(x) for x in i.split(",")]
    j = [int(x) for x in j.split(",")]
    start.append(i)
    end.append(j)
p2 = True
d = defaultdict(int)
for i in range(len(start)):
    if start[i][0] == end[i][0]:
        for j in range(min(start[i][1], end[i][1]), max(start[i][1], end[i][1]) + 1):
            d[(start[i][0]), j] += 1
    if start[i][1] == end[i][1]:
        for j in range(min(start[i][0], end[i][0]), max(start[i][0], end[i][0]) + 1):
            d[(j, start[i][1])] += 1
    if p2:
        if abs(start[i][0] - end[i][0]) == abs(start[i][1] - end[i][1]):
            if start[i][0] > end[i][0]:
                dx = -1
            else:
                dx = 1
            if start[i][1] > end[i][1]:
                dy = -1
            else:
                dy = 1
            x, y = start[i]
            while(x != end[i][0] and y != end[i][1]):
                d[(x, y)] += 1
                x += dx
                y += dy
            d[(x, y)] += 1
        

print(sum(i > 1 for i in d.values()))
    