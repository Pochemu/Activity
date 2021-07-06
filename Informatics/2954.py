n = int(input())
k = int(input())
i = n - k % n
print(i * (k % n != 0))