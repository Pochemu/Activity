for a in range(1, 1000):
    flag = True
    for x in range(1, 100):
        if not(not(x%a==0) or not(x%21 == 0) or x%35 == 0):
            flag = False
    if flag == True:
        print(a)