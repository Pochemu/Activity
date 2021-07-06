n = int(input())
num_array = list(map(int, input().split()))
answer = 0
for i in range(0, n):
    if num_array[i] > 0:
        answer += 1
print(answer)