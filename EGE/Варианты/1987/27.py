f = open('27-9b.txt')
n = int(f.readline())
buf = []
ans = 0
a = 10001
b = 10001
ans = 10001 * 10001
for _ in range(6):
    buf.append(int(f.readline()))
for _ in range(6, n):
    x = int(f.readline())
    if buf[0] % 2:
        a = min(buf[0], a)
    if x % 2:
        ans = min(ans, x*a)
    del buf[0]
    buf.append(x)
print(ans)