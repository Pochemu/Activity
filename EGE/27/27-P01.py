f = open('../../../../В процессе/test.txt')
n = int(f.readline())
d_ost = [10001] * 6
sum_max = 0
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_max += max(a, b)
    d = abs(a-b)
    r = d%6
    if r != 0:
        k1 = d_ost.copy()
        for i in range(6):
            r1 = (r + i) % 6
            k1[r1] = min(k1[r1], d+d_ost[i])
        k1[r] = min(d, k1[r])
        d_ost = k1.copy()
print(sum_max - d_ost[sum_max%6])
print(d_ost)