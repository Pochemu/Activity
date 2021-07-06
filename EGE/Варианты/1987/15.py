for a in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y+3*x != 60) or (x > a) or (y > a)) == 0:
                k = 0
    if k == 1:
        print(a)