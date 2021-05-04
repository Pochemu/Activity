cnt = 0


def F(n):
    if n <= 18:
        return n + 3
    elif n % 3 == 0:
        return (n//3)*F(n//3) + n - 12
    else:
        return F(n-1) + n*n + 5


for i in range(1, 801):
    for j in str(F(i)):
        if int(j) % 2 == 1:
            break
    else:
        cnt += 1
print(cnt)