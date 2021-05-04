def F(n):
    if n > 30:
        return n**2 + 5*n + 4
    elif n % 2 == 0:
        return F(n+1) + 3*F(n+4)
    else:
        return 2*F(n+2) + F(n+5)


cnt = 0
for i in range(1, 1001):
    numbers = F(i)
    sum_n = 0
    numbers = str(numbers)
    for j in range(len(numbers)):
        sum_n += int(numbers[j])
    if sum_n == 27:
        cnt += 1
print(cnt)