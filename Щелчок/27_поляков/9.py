f = open('27-9b.txt')
n = int(f.readline())
buf = []
min_a = 10001
ans = 100000000
for _ in range(6):
    x = int(f.readline())
    buf.append(x)
for _ in range(6, n):
    x = int(f.readline())
    if buf[0]%2 == 1:
        min_a = min(min_a, buf[0])
    if x%2 == 1:
        ans = min(min_a * x, ans)
    buf.append(x)
    del buf[0]
print(ans)