f = open('27-34b.txt')
n = int(f.readline())
sum_min = 0
z = [0] * 3
ost = [10001] * 6
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a+b
    z[1] = a+c
    z[2] = b+c
    z.sort()
    sum_min += z[0]
    ost1 = ost.copy()
    for j in range(1, 3):
        d = z[j] - z[0]
        r = d%6
        if r != 0:
            for i in range(1, 6):
                r1 = (r + i) % 6
                ost1[r1] = min(ost1[r1], d+ost[i])
            ost1[r] = min(ost1[r], d)
    ost = ost1.copy()
if sum_min%6 == 0:
    print(sum_min)
else:
    if sum_min%6 > 6:
        print(sum_min + ost[10 - (sum_min%6 - 6)])
    else:
        print(sum_min + ost[6 - sum_min%6])