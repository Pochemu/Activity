f = open('../../../../В процессе/test.txt')
n = int(f.readline())
d_min = 10001
sum_max = 0
for _ in range(n):
    a, b = map(int, f.readline().split())
    sum_max += max(a,b)
    d = abs(a-b)
    if d%3 != 0:
        d_min = min(d_min, d)
print(sum_max - d_min)