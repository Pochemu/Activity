numbers = []
with open('27-12a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (numbers[i] * numbers[j]) % 6 == 0:
            ans += 1
print(ans)