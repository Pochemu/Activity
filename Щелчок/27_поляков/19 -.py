f = open('27-19b.txt')
n = int(f.readline())
x = int(f.readline())
max_minus = -101
d_min = x
d_max = x
ans = x
for _ in range(n-1):
    x = int(f.readline())
    d = min(d_min * x, min(d_max * x, x))
    d_max = max(d_min*x, max(d_max*x, x))
    d_min = d
    ans = max(ans, d_max)
print(ans)