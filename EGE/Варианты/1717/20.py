def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    elif (k1 + k2 < w and step == 3) or (k1 + k2 >= w):
        return False
    else:
        if step%2 == 0:
            return (f(k1+1, k2, w, step + 1) or
                    f(k1, k2+1, w, step + 1) or
                    f(k1*2, k2, w, step + 1) or
                    f(k1, k2*2, w, step + 1))
        else:
            return (f(k1 + 1, k2, w, step + 1) and
                    f(k1, k2 + 1, w, step + 1) and
                    f(k1 * 2, k2, w, step + 1) and
                    f(k1, k2 * 2, w, step + 1))


for s in range(1, 31):
    if f(9, s, 40, 0):
        print(s)