f = open('27-7b.txt')
n = int(f.readline())
d_7 = 0
d = 0
for _ in range(n):
    x = int(f.readline())
    if x%7 == 0 and x % 49 != 0:
        d_7 = max(d_7, x)
    elif x % 49 != 0:
        d = max(d, x)
print(d_7 * d)