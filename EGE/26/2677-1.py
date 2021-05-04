num = []
ans = 0
with open('27-17a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        num.append(int(f.readline()))
for i in range(n-6):
    for j in range(i+5, n):
        if (num[i] + num[j])%2 and (num[i]*num[j])%13 == 0:
            ans += 1
print(ans)