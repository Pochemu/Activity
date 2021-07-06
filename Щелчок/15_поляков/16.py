def f(n):
    if n <= 1:
        return 1
    elif n%2:
        return n*n + f(n-2)
    else:
        return n + f(n-1)


print(f(80))