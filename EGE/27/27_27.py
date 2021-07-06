f = open('27-27b.txt')
n = int(f.readline())
ans = 0
min_d = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    ans += max(a, b)
    d = abs(a-b)
    if d%16 != 0:
        min_d = min(d, min_d)
if ans%16 == 10:
    print(ans-min_d)
else:
    print(ans)