f = open('27-29b.txt')
n = int(f.readline())
sum_max = 0
d_min = 10001
z = [0] * 3
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a + b
    z[1] = b + c
    z[2] = a + c
    z.sort()
    sum_max += z[2]
    for j in range(2):
        d = z[2] - z[j]
        if d % 5 != 0:
            d_min = min(d_min, d)
if sum_max%5:
    print(sum_max)
else:
    print(sum_max - d_min)