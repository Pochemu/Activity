f = open('26-j1.txt')
n = int(f.readline())
coins = [0] * 100
ans = 0
for _ in range(n):
    x = int(f.readline())
    if coins[100-x] >= 1:
        ans += 1
        coins[100-x] -= 1
    else:
        coins[x%100] += 1
print(ans)
