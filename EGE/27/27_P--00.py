f = open('27.txt')
n = int(f.readline())
s = 0
dMin = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a-b)
    if d % 3 > 0:
        dMin = min(d, dMin)
f.close()
if s % 3 != 0:
    print(s)
else:
    print(s-dMin)