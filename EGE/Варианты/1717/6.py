for i in range(1, 1000):
    d = i
    n = 3
    s = 38
    while s <= 1200:
        s = s + d
        n = n + 7
    if n == 150:
        print(i)