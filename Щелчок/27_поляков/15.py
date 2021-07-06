f = open('27-15b.txt')
n = int(f.readline())
ost = [0] * 14
buf = []
ans = 0
for _ in range(5):
    x = int(f.readline())
    buf.append(x)
for _ in range(5, n):
    x = int(f.readline())
    ost[buf[0]%14] += 1
    ans += ost[(14 - x%14)%14]
    buf.append(x)
    del buf[0]
print(ans)