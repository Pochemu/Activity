f = open('27-34b.txt')
n = int(f.readline())
sum_min = 0
d_ost = [10001] * 6
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z = [0] * 3
    z[0] = a+b
    z[1] = b+c
    z[2] = a+c
    z.sort()
    sum_min += z[0]
    d_ost1 = d_ost.copy()
    for j in range(1, 3):
        d = z[j] - z[0]
        r = d%6
        if r != 0:
            for i in range(1, 6):
                r1 = (r + i)%6
                d_ost1[r1] = min(d_ost1[r1], d + d_ost[i])
            d_ost1[r] = min(d_ost1[r], d)
    d_ost = d_ost1.copy()
if sum_min%6 != 0:
    print(sum_min + d_ost[6-sum_min%6])
else:
    print(sum_min)
