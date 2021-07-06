f = open('test.txt')
n = int(f.readline())
sum_max = 0
sum_min = 0
ost = [10001] * 5
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_max += max(a, b)
    sum_min += min(a, b)
    d = abs(a-b)
    r = d%5
    if r != 0:
        ost[r] = min(ost[r], d)
    else:
        ost[0] = d
if sum_max%5 == 0:
    if sum_min%3 == 0:
        print(sum_max - min(ost[1:5]))
        print(sum_min + min(ost[1:5]))
    else:
        print(sum_max - ost[0])
        print(sum_min + ost[0])
else:
    if sum_max%3 == 0:
        print()

