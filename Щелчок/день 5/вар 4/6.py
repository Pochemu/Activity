for i in range(-10000, 10000000000):
    k = i
    n = -100
    s = -10
    while n+s < 10:
        n = n + k
        k = k + 1
        s = s*k
    print(n)