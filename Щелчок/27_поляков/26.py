f = open('27-26b.txt')
n = int(f.readline())
ost = [10001] * 16
sum_min = 0
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_min += min(a, b)
    d = abs(a - b)
    r = d%16
    if r != 0:
        ost1 = ost.copy()
        for i in range(1, 16):
            r1 = (r + i)%16
            ost1[r1] = min(ost1[r1], d + ost[i])
        ost1[r] = min(ost1[r], d)
        ost = ost1.copy()
if sum_min % 16 == 15:
    print(sum_min)
else:
    print(sum_min + ost[16 - sum_min%16 - 1])