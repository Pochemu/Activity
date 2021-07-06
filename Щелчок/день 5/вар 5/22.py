for i in range(1, 1000000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 2
        b = b * (x%1000)
        x = x // 1000
    if a == 4 and b == 13:
        print(i)