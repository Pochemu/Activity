n = int(input())
result = (n // 1000 == n % 10) * (n // 100 % 10 == n // 10 % 10)
print(result)
