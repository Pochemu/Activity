import math
cnt = 0
f = open('../../../В процессе/26-j2.txt')
n = int(f.readline())
numbers = []
for i in range(n):
    numbers.append(int(f.readline()))
numbers.sort()
middle = numbers[n//2]
mean = math.ceil(sum(numbers) / n)
for i in range(n):
    if mean <= numbers[i] <= middle:
        cnt += 1
print(cnt)