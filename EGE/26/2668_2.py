buf = []
f = open('2668-b.txt')
n = int(f.readline())
m = 10001
answer = 10000**2 * 2 + 1
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(5, n):
    x = int(f.readline())
    m = min(m, buf[0])
    answer = min(answer, x**2 + m**2)
    del buf[0]
    buf.append(x)
print(answer)
f.close()