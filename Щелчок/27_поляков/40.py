f = open('27-40b.txt')
n = int(f.readline())
z = [0] * 3
sum_max = 0
g1 = 0
g2 = 0
d_min = 10001
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a
    z[1] = b
    z[2] = c
    z.sort()
    sum_max += z[2]
    g1 += z[0]
    g2 += z[1]
    d1 = z[2] - z[0]
    d2 = z[2] - z[1]
    if d1 % 2 == 1:
        d_min = min(d_min, d1)
    if d2 % 2 == 1:
        d_min = min(d_min, d2)
print(g1, g2)
print(sum_max)
print(d_min)