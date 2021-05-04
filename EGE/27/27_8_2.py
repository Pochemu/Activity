f = open('27-8b.txt')
n = int(f.readline())
m = 1001
answer = 1000001
buf = []
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(5, n):
    x = int(f.readline())
    if buf[0] < m:
        m = buf[0]
    answer = min(answer, x**2 + m**2)
    del buf[0]
    buf.append(x)
print(answer)
f.close()