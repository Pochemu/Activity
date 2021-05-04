coins = []
cnt = 0
with open('26-j1.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        coins.append(int(f.readline()))
for i in range(n):
    for j in range(n-1, i, -1):
        if coins[i] + coins[j] == 100:
            cnt += 1
            coins[i] = coins[j] = 0
print(cnt)
