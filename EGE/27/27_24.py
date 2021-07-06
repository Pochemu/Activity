f = open('27-24b.txt')
n = int(f.readline())
dMin = 100001
s = 0
for _ in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a-b)
    dMin = min(d, dMin)
if s%10 != 6:
    print(s)
else:
    print(s + dMin)