def counter(n):
    if n <= 3:
        x = n
    else:
        if n%2 == 0:
            x = n + 3 + counter(n - 1)
        else:
            x = n * n + counter(n - 2)
    if x % 7 == 0:
        return 1
    else:
        return 0


answer = 0
for i in range(1, 1001):
    answer = answer + int(counter(i))
print(answer)
