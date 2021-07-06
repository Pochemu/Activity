f = open('27-24b.txt')
n = int(f.readline())
sum_min = 0
d_min = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_min += min(a, b)
    d = abs(a - b)
    if d%10 != 0:
        d_min = min(d_min, d)
if sum_min%10 == 6:
    print(sum_min + d_min)
else:
    print(sum_min)