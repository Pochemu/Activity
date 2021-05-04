answer = 0
numbers = []
with open('27-14a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
for i in range(n-1):
    for j in range(i+1, n):
        if (numbers[i]+numbers[j])%12 == 0:
            answer += 1
print(answer)