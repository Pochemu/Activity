f = open('27-8b.txt')
n = int(f.readline())
buf = []
ans = 1000001
a = 1001
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(n-5):
    x = int(f.readline())
    a = min(a, buf[0])
    ans = min(ans, a ** 2 + x ** 2)
    del buf[0]
    buf.append(x)
print(ans)