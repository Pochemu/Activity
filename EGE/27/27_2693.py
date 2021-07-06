f = open('27-33b.txt')
n = int(f.readline())
sum_max = 0
d_min = [10001] * 4
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z = [0] * 3
    z[0] = a+b
    z[1] = b+c
    z[2] = c+a
    z.sort()
    sum_max += z[2]
    d_min1 = d_min.copy()
    for j in range(2):
        d = z[2] - z[j]
        r = d % 4
        if r != 0:
            for i in range(1, 4):
                r1 = (r+i)%4
                d_min1[r1] = min(d_min1[r1], d + d_min[i])
            d_min1[r] = min(d_min1[r], d)
    d_min = d_min1.copy()
if sum_max%4 == 0:
    print(sum_max)
else:
    print(sum_max - d_min[sum_max % 4])
