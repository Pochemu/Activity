numbers = []
cnt = 0
with open('27-18b.txt') as f:
    n = int(f.readline())
    for i in range(n):
        numbers.append(int(f.readline()))
for i in range(n-1):
    for j in range(i+1, i+5):
        if j<n:
            if j-i < 5:
                if not (numbers[i] * numbers[j]) % 13:
                    if (numbers[i] + numbers[j]) % 2:
                        cnt += 1
                        print(numbers[i], numbers[j])
print(cnt)