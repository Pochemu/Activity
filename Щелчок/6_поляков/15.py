for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        if (x%a!=0) or (x%21!=0) or (x%18 == 0):
            ok = 0
    if ok == 1:
        print(a)