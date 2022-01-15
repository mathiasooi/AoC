from statistics import median, mean
xs = sorted([int(i) for i in open("input.txt").read().split(",")])
print(int(sum(abs(i - median(xs)) for i in xs)))
print(int(sum((abs(i - int(mean(xs)))*(abs(i-int(mean(xs)))+1))/2 for i in xs)))

