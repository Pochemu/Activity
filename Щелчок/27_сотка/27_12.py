f = open('27B.txt')
n = int(f.readline())
d = 10001
d_3 = 10001
d_5 = 10001
d_15 = 10001
for _ in range(n):
    x = int(f.readline())
    if x >= 1:
        if x%15 == 0:
            d_15 = min(d_15, x)
        elif x%5 == 0:
            d_5 = min(d_5, x)
        elif x%3 == 0:
            d_3 = min(d_3, x)
        else:
            d = min(d, x)
print(min(d*d_15, d_15*d_3, d_3 * d_5, d_15 * d_5))