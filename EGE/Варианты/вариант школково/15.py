for a in range(1, 100):
    ok = True
    for k in range(1, 100):
        for n in range(1, 100):
            if not(((5*k + 6*n) > 57) or ((k <= a) and (n < a))):
                ok = False
                break
    if ok:
        print(a)