n = int(input())
num_array = list(map(int, input().split()))
answer_array =[]
for i in range(0, n):
    if num_array[i]%2 == 0:
        answer_array.append(num_array[i])
print(*answer_array)