def F(n):
    if n <= 1:
        return 1
    elif n%2:
        return n + F(n-2)
    else:
        return n*F(n-1)
print(F(84))