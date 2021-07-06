n = int(input())
num_array = list(map(int, input().split()))
def answer(n, num_array):
    for i in range(1, n):
        if (num_array[i-1] >= 0 and num_array[i] >= 0) or (num_array[i-1] < 0 and num_array[i] < 0):
            return "YES"
    return "NO"
print(answer(n, num_array))