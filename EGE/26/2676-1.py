numbers = []
ans = 0
with open('27-16a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
for i in range(n-1):
    for j in range(i+1, n):
        if (numbers[i] + numbers[j]) % 2 and (numbers[i] * numbers[j]) % 13 == 0:
            ans += 1
print(ans)