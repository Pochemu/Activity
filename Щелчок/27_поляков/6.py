f = open('27-6b.txt')
n = int(f.readline())
d_6 = 0
pmd_6 = 0
d_3 = 0
d_2 = 0
d = 0
for _ in range(n):
    x = int(f.readline())
    if x%6 == 0:
        if x >= d_6:
            pmd_6 = d_6
            d_6 = x
    elif x%3 == 0:
        d_3 = max(d_3, x)
    elif x%2 == 0:
        d_2 = max(d_2, x)
    else:
        d = max(d, x)
print(max(d*d_6, pmd_6 * d_6, d_3 * d_2, d_3 * d_6, d_2 * d_6))