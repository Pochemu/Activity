f = open('27-14b.txt')
n = int(f.readline())
ost = [0] * 12
ans = 0
for _ in range(n):
    x = int(f.readline())
    ost[x%12] += 1
for i in range(1, 6):
    ans += ost[i] * ost[12 - i]
ans += (ost[6] * (ost[6] - 1))//2
ans += (ost[0] * (ost[0] - 1))//2
print(ans)