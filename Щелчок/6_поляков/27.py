f = open('27-28b.txt')
n = int(f.readline())
sum_min = 0
d_min = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a-b)
    if d%8 != 0:
        d_min = min(d_min, d)
    sum_min += min(a, b)
if sum_min%8 != 2:
    print(sum_min)
else:
    print(sum_min+d_min)