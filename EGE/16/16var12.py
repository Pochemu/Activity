answer = 0


def F(n):
    if n > 25:
        return 2*n*n*n + n*n
    else:
        return F(n+2) + 2*F(n+3)


print(sum(map(int, str(F(2)))))