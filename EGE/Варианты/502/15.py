for i in range(1, 1000):
    a = i
    ok = 1
    for x in range(1, 1000):
        if not((x&49 != 0) or (x&28 == 0) or (x&i != 0)):
            ok = 0
    if ok == 1:
        print(a)
        break