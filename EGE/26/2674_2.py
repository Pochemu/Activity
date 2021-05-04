f = open('27-14b.txt')
n = int(f.readline())
num = [0] * 12
ans = 0
num[int(f.readline()) % 12] += 1
for i in range(1, n):
    x = int(f.readline())
    ans += num[(12 - (x % 12))%12]
    num[x % 12] += 1
print(num)
print(ans)
