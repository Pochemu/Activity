n = int(input())
num_array = list(map(int, input().split()))
answer_array =[]
for i in range(n-1, -1, -1):
    answer_array.append(num_array[i])
print(*answer_array)