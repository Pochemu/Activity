f = open('27-23b.txt')
n = int(f.readline())
sum_max = 0
d_min = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_max += max(a, b)
    d = abs(a - b)
    if d%10 != 0:
        d_min = min(d, d_min)
if sum_max%10 == 5:
    print(sum_max - d_min)
else:
    print(sum_max)