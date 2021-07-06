f = open('27-33b.txt')
n = int(f.readline())
sum_max = 0
ost = [10001] * 4
z = [0] * 3
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a+b
    z[1] = a+c
    z[2] = b+c
    z.sort()
    sum_max += z[2]
    ost1 = ost.copy()
    for j in range(2):
        d = z[2] - z[j]
        r = d%4
        if r != 0:
            for i in range(1, 4):
                r1 = (r + i)%4
                ost1[r1] = min(ost1[r1], d + ost[i])
            ost1[r] = min(ost1[r], d)
    ost = ost1.copy()
if sum_max%4 == 0:
    print(sum_max)
else:
    print(sum_max - ost[sum_max%4])