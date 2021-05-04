cnt = 0


def F(n):
    if n <= 3:
        return n
    elif n%2 == 0:
        return F(n-1) + 2 * F(n / 2)
    else:
        return F(n-1) + F(n-3)


i = 0
while True:
    i += 1
    if F(i) < 1e8:
        cnt += 1
    else:
        break
print(cnt)