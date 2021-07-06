n = int(input())
num_array = list(map(int, input().split()))
answer_array = []
if n % 2 != 0:
    x = n-1
else:
    x = n
for i in range(0, x, 2):
    answer_array.append(num_array[i + 1])
    answer_array.append(num_array[i])
if n % 2 != 0:
    answer_array.append(num_array[n - 1])
print(*answer_array)
