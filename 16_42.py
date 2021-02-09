def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) + 3 * G(n-1)


def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) - 2 * G(n-1)


answer = 0
for i in str(F(18)):
    answer += int(i)
print(answer)