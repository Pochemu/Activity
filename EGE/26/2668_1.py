numbers = []
answer = 10000**2 * 2 + 1
with open('2668-a.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        numbers.append(int(f.readline()))
for i in range(n-5):
    for j in range(i+5, n):
        answer = min(answer, numbers[i]**2 + numbers[j]**2)
print(answer)
