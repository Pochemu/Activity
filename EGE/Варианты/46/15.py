for a in range(1, 500):
    ok = 1
    for x in range(1, 1001):
        if not(not(not(x%40) or not(x%64)) or not(x%a)):
            ok = 0
    if ok == 1:
        print(a)