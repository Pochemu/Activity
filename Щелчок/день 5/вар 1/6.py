for i in range(10, 1000):
    k = i
    n = 2
    s = 5124
    while s + n > 100:
        s = s-k
        n = n+(s%10)
    if n == 24:
        print(i)