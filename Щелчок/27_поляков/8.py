f = open('27-8b.txt')
n = int(f.readline())
buf = []
min_a = 10001
ans = 100000000
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(5, n):
    x = int(f.readline())
    min_a = min(min_a, buf[0])
    ans = min(ans, min_a **2 + x**2)
    buf.append(x)
    del buf[0]
print(ans)