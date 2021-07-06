f = open('27-22a.txt')
n = int(f.readline())
ans = 0
dm = [10000]*10
for _ in range(n):
    a, b = map(int, f.readline().split())
    ans += min(a, b)
    d = abs(a-b)
    ost = d%10
    if ost > 0:
        dm_1 = dm
        for i in range(1, 10):
            ost_1 = (ost + i)%10
            dm_1[ost_1] = min(dm_1[ost_1], d+dm[i])
        dm_1[ost] = min(d, dm_1[ost])
        dm = dm_1
if ans % 10 == 4:
    print(ans)
else:
    x = 4 - ans%10
    if x < 0:
        x += 10
    print(ans+dm[x])
