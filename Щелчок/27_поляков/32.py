f = open('27-32b.txt')
n = int(f.readline())
sum_min = 0
ost = [10001] * 11
z = [0] * 3
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a
    z[1] = b
    z[2] = c
    z.sort()
    sum_min += z[0]
    ost1 = ost.copy()
    for j in range(1, 3):
        d = z[j] - z[0]
        r = d % 11
        if r != 0:
            for i in range(1, 11):
                r1 = (r + i)%11
                ost1[r1] = min(ost1[r1], d + ost[i])
            ost1[r] = min(ost1[r], d)
    ost = ost1.copy()
if sum_min%11 == 0:
    print(sum_min)
else:
    print(sum_min + ost[11 - (sum_min%11)])