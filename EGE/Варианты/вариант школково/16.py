def f(n):
    if n < 5:
        return n
    else:
        return 5*f(n-1) + 2*f(n-2)


print(f(10))