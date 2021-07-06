for i in range(1, 1000):
    k = i
    n = 1
    s = 0
    while n * s < 1234:
        n = n * k
        s = s + k
    if n == 1024:
        print(i)