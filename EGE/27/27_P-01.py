f = open('27.txt')
n = int(f.readline())
dMin = [10001] * 6
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    r = d%6
    if r > 0:
        dMinNew = dMin.copy()
        for k in range(1, 6):
            r0 = (r+k)%6
            dMinNew[r0] = min(d+dMin[k], dMinNew[r0])
        dMinNew[r] = min(d, dMinNew[r])
        dMin = dMinNew.copy()
if s % 6 == 0:
    print(s)
else:
    print(s - dMin[s%6])