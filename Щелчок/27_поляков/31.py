f = open('27-31b.txt')
n = int(f.readline())
sum_min = 0
d_min = 10001
z = [0] * 3
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a + b
    z[1] = a + c
    z[2] = c + b
    z.sort()
    sum_min += z[0]
    for j in range(1, 3):
        d = z[j] - z[0]
        if d%9 != 0:
            d_min = min(d_min, d)
if sum_min % 9:
    print(sum_min)
else:
    print(sum_min + d_min)