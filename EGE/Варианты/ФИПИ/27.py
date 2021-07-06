f = open('27_B.txt')
n = int(f.readline())
d_min = 10000000
sum_max = 0
z = [0] * 3
for _ in range(n):
    a, b, c = map(int,f.readline().split())
    z[0] = a
    z[1] = b
    z[2] = c
    z.sort()
    sum_max += z[2]
    for j in range(1, 3):
        d = z[j] - z[0]
        r = d % 109
        if r != 0:
            d_min = min(d, d_min)
if sum_max % 109 == 0:
    print(sum_max + d_min)
else:
    print(sum_max)