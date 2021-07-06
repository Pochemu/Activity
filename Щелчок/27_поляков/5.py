f = open('27-5a.txt')
n = int(f.readline())
sum_min = 0
ost = [10001] * 5
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_min += min(a, b)
    d = abs(a - b)
    r = d%5
    if r != 0:
        ost1 = ost.copy()
        for i in range(1, 5):
            r1 = (r + i) % 5
            ost1[r1] = min(ost1[r1], d + ost[i])
        ost1[r] = min(ost1[r], d)
        ost = ost1.copy()
if sum_min % 5 == 0:
    print(sum_min)
else:
    print(sum_min + ost[5-(sum_min%5)])