for i in range(1, 1000000):
    x = i
    a = 0
    b = 0
    d = 0
    while x > 0:
        if d % 2 == 0:
            a += x%10
        else:
            b += x%10
        x = x//10
        d += 1
    if a == 4 and b == 15:
        print(i)
        break