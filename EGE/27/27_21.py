f = open('27-21a.txt')
n = int(f.readline())
max_sum = 0
min_d = [10001] * 10
for _ in range(n):
    a, b = map(int, f.readline().split())
    max_sum += max(a, b)
    d = abs(a-b)
    ost = d % 10
    if ost > 0:
        min_d_copy = min_d.copy()
        for i in range(1, 10):
            ost_all = (ost + i) % 10
            min_d_copy[ost_all] = min(min_d_copy[ost_all], d+min_d[i])
        min_d_copy[ost] = min(d, min_d_copy[ost])
        min_d = min_d_copy
if max_sum % 10 == 8:
    print(max_sum)
else:
    print(max_sum - min_d[(max_sum - 8) % 10])