numbers = []
cnt = 0
with open('27-17a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
for i in range(n-5):
    for j in range(i+5, n):
        if (numbers[i] + numbers[j]) % 2 and (numbers[i] * numbers[j]) % 13 == 0:
            cnt += 1
print(cnt)