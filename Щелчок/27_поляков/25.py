f = open('27-25a.txt')
n = int(f.readline())
sum_max = 0
ost = [10001] * 8
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_max += max(a, b)
    d = abs(a - b)
    r = d%8
    if r != 0:
        ost1 = ost.copy()
        for i in range(1, 8):
            r1 = (r + i)%8
            ost1[r1] = min(ost1[r1], d + ost[i])
        ost1[r] = min(ost1[r], d)
        ost = ost1.copy()
if sum_max % 8 == 3:
    print(sum_max)
else:
    if sum_max % 8 > 3:
        print(sum_max - ost[sum_max % 8 - 3])
    else:
        print(sum_max - ost[8 - sum_max % 8 + 1])