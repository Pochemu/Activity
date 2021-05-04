numbers = []
f = open('27-9a.txt')
n = int(f.readline())
answer = 1000001
m = 1001
for _ in range(6):
    numbers.append(int(f.readline()))
for i in range(6, n):
    x = int(f.readline())
    if numbers[0] % 2 and numbers[0] < m:
        m = numbers[0]
    if x * m < answer and x % 2:
        answer = x * m
    del numbers[0]
    numbers.append(x)
if answer == 1000001:
    print(-1)
else:
    print(answer)
