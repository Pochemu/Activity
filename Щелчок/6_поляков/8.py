for i in range(1, 1000):
    s = i
    n = 1
    while s < 62:
        s = s + 7
        n = n * 3
    if n == 729:
        print(i)