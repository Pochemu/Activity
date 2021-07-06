f = open('27-2b.txt')
n = int(f.readline())
sum_max = 0
ost = [10001] * 3
for _ in range(n):
    a, b = map(int,f.readline().split())
    d = abs(a-b)
    sum_max += max(a, b)
    r = d%3
    if r != 0:
        ost1 = ost.copy()
        for i in range(1, 3):
            r1 = (r + i)%3
            ost1[r1] = min(ost1[r1], d + ost[i])
        ost1[r] = min(ost1[r], d)
        ost = ost1.copy()
if sum_max % 3 == 0:
    print(sum_max)
else:
    print(sum_max - ost[sum_max%3])
