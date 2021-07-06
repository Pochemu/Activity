for a in range(1, 1000000):
    flag = True
    for x in range(1, 50):
        for y in range(1, 100):
            if ((2*x + y != 70) or (x < y) or (a < x)) == 0:
                flag = False
    if flag:
        print(a)