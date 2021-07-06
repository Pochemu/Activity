f = open('27-18b.txt')
n = int(f.readline())
buf = []
buf.append(int(f.readline()))
ans = 0
for i in range(1, 4):
    x = int(f.readline())
    for j in range(0, i):
        if ((x + buf[j]) % 2) and ((x * buf[j]) % 13 == 0):
            ans += 1
    buf.append(x)
for _ in range(4, n):
    x = int(f.readline())
    for j in range(0, 4):
        if ((x + buf[j]) % 2) and ((x * buf[j]) % 13 == 0):
            ans += 1
    buf.append(x)
    del buf[0]
print(ans)