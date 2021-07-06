f = open('27-63b.txt')
n = int(f.readline())
sum_min = [(10**8)+1, (10**8)+1, (10**8)+1, (10**8)+1]
for _ in range(n):
    x = int(f.readline())
    d1 = sum_min[0] - x
    d2 = sum_min[1] - x
    d3 = sum_min[2] - x
    d4 = sum_min[3] - x
    d_max = 0
    if d1 > 0:
        d_max = max(d_max, d1)
    if d2 > 0:
        d_max = max(d_max, d2)
    if d3 > 0:
        d_max = max(d_max, d3)
    if d4 > 0:
        d_max = max(d_max, d4)
    if d_max == d1:
        sum_min[0] = x
    elif d_max == d2:
        sum_min[1] = x
    elif d_max == d3:
        sum_min[2] = x
    elif d_max == d4:
        sum_min[3] = x
print(sum(sum_min))