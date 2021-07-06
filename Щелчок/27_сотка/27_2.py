f = open('27A.txt')
n = int(f.readline())
d = [[] for _ in range(29)]
ans_m = 10001
ans = []
for _ in range(n):
    x = int(f.readline())
    if len(d[x%29]) == 0:
        d[x % 29].append(x)
    else:
        for i in range(len(d[x%29])):
            if ans_m > abs(d[x%29][i] - x):
                ans_m = abs(d[x%29][i] - x)
                ans = [d[x%29][i], x]
        d[x%29].append(x)
print(*ans)