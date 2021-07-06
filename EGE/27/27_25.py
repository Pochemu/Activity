f = open('27-25b.txt')
n = int(f.readline())
max_sum = 0
min_d = [10001] * 8
for _ in range(n):
    a, b = map(int, f.readline().split())
    max_sum += max(a, b)
    d = abs(a-b)
    ost = d % 8
    if ost > 0:
        min_d_copy = min_d.copy()
        for i in range(1, 8):
            ost_check = (ost + i) % 8
            min_d_copy[ost_check] = min(min_d_copy[ost_check], d + min_d[i])
        min_d_copy[ost] = min(d, min_d_copy[ost])
        min_d = min_d_copy
if max_sum % 8 == 3:
    print(max_sum)
else:
    print(max_sum - min_d[(max_sum-3) % 8])