f = open('27B.txt')
n = int(f.readline())
d_min = [10001] * 13
ans = 10001
for _ in range(n):
    x = int(f.readline())
    d_min[x % 13] = min(d_min[x%13], x)
for i in range(1, 7):
    ans = min(ans, d_min[i] + d_min[13-i])
print(ans)