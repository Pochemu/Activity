numbers = []
with open('27-13a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
cnt = 0
for i in range(n-7):
    for j in range(i+7, n):
        if (numbers[i] * numbers[j]) % 14 == 0:
            cnt += 1
print(cnt)