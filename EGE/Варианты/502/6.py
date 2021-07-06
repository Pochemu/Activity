for i in range(1, 200):
    for j in range(1, 1000):
        s = i
        x = j
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 17:
            print(j, i)
            break