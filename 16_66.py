def F(n):
    if n <= 15:
        return n * n + 11
    elif n%2 == 0:
        return F(n // 2) + n * n * n - 5 * n
    else:
        return F(n-1) + 2 * n + 3


answer = 0
for i in range(1, 1001):
    if str(F(i)).count('6') >= 3:
        answer += 1
print(answer)