f = open('27-13b.txt')
n = int(f.readline())
k14 = 0
k7 = 0
k2 = 0
k = 0
buf = []
ans = 0
for _ in range(7):
    buf.append(int(f.readline()))
for _ in range(7, n):
    x = int(f.readline())
    if buf[0] % 14 == 0:
        k14 += 1
    elif buf[0] % 7 == 0:
        k7 += 1
    elif buf[0] % 2 == 0:
        k2 += 1
    else:
        k += 1
    if x % 14 == 0:
        ans += k14 + k7 + k2 + k
    elif x % 7 == 0:
        ans += k2 + k14
    elif x % 2 == 0:
        ans += k7 + k14
    else:
        ans += k14
    buf.append(x)
    del buf[0]
print(ans)