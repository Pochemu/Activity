n = int(input())
num_array = list(map(int, input().split()))
answer_array = [num_array[n-1]]
for i in range(0, n-1):
    answer_array.append(num_array[i])
print(*answer_array)