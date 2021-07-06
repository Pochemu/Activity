for a in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((2*x + 3*y) > 30) or (x + y <= a)) == 0:
                flag = False
    if flag == True:
        print(a)
        break