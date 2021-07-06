f = open('27-22b.txt')
n = int(f.readline())
sum_min = 0
ost = [10001] * 10
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_min += min(a, b)
    d = abs(a-b)
    r = d%10
    if r != 0:
        ost1 = ost.copy()
        for i in range(1, 10):
            r1 = (r + i)%10
            ost1[r1] = min(ost1[r1], d + ost[i])
        ost1[r] = min(ost1[r], d)
        ost = ost1.copy()
if sum_min % 10 == 4:
    print(sum_min)
else:
    if sum_min%10 < 4:
        print(sum_min + ost[4 - sum_min%10])
    else:
        print(sum_min + ost[(14 - sum_min%10)])