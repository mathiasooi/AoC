fish = [int(i) for i in open("input.txt").read().split(",")]
# def simulate():
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             fish[i] = 6
#             fish.append(8)
#         else:
#             fish[i] -= 1
# for i in range(256):
#     print(i)
#     simulate()
# print(len(fish))

def solve(days):
    d = [0]*9
    for i in fish:
        d[i] += 1
    for _ in range(days):
        x = d[0]
        for i in range(1, 9):
            d[i-1] = d[i]
        d[6] += x
        d[8] = x
    return sum(d)
print(solve(80))
print(solve(256))