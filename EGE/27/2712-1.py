ans = 0
num = []
with open('27-37a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        num.append(int(f.readline()))
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if num[i] + num[j] == num[k]:
                ans += 1
print(ans)