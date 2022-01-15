s = [int(i) for i in open("input.txt").read().split()]
print(sum(s[i+1] > s[i] for i in range(len(s)-1)))
print(sum(s[i+3] > s[i] for i in range(len(s)-3)))
