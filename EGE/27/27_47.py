f = open('27-47b.txt')
n = int(f.readline())
min_sum = 0
max_sum = 0
min_d = [10001] * 10
for _ in range(n):
    a, b = map(int, f.readline().split())
    if a > b:
        max_sum += a
        min_sum += b
    else:
        max_sum += b
        min_sum += a
    d = abs(a - b)
    ost = d % 10
    if ost > 0:
        min_d_copy = min_d.copy()
        for i in range(1, 10):
            ost_check = (ost + i) % 10
            min_d_copy[ost_check] = min(min_d_copy[ost_check], d + min_d[i])
        min_d_copy[ost] = min(d, min_d_copy[ost])
        min_d = min_d_copy
if max_sum % 10 == min_sum % 10:
    print(min_sum)
else:
    print(min_sum + min_d[(max_sum - min_sum % 10) % 10])
