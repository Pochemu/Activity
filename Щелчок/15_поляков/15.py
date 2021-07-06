for a in range(1, 100):
    ok = 1
    for x in range(1, 1000):
        if not(x%18 == 0 or x%21 == 0 or x%a):
            ok = 0
    if ok == 1:
        print(a)