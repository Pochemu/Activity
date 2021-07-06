n = int(input())
num_array = list(map(int, input().split()))
answer = 0
for i in range(1, n):
    if num_array[i] > num_array[i-1]:
        answer += 1
print(answer)