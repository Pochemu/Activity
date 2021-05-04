numbers = []
with open('27-8a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
min_ans = 1000000
for i in range(n-5):
    for j in range(i+5, n):
            min_ans = min(numbers[i]**2 + numbers[j]**2, min_ans)
print(min_ans)