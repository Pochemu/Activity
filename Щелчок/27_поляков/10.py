f = open('27-10b.txt')
n = int(f.readline())
d_min = 10001
z = [0] * 3
sum_max = 0
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a
    z[1] = b
    z[2] = c
    z.sort()
    sum_max += z[2]
    for j in range(2):
        d = z[2] - z[j]
        if d%4 != 0:
            d_min = min(d_min, d)
if sum_max%4 == 0:
    print(sum_max - d_min)
else:
    print(sum_max)