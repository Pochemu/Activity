def f(n):
    if n < 10:
        return n
    elif n > 9:
        return f(n) * f(n-2)


def g(n):
    if n < 11:
        return n*3
    if n > 10 and n%7:
        return f(n**2) + f(n**2 + 1) + f(n ** n)


print(g(10) + f(2) + f(5))