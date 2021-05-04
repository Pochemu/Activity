def F(n):
    if n > 25:
        return 2 * n * n * n + n * n
    else:
        return F(n+2) + 2 * F(n+3)


answer = 0
for i in str(F(2)):
    answer += int(i)
print(answer)