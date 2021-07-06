def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 4 or step == 2):
        return True
    elif k1 + k2 >= w and (step == 1 or step == 3) or k1 + k2 < w and step == 4:
        return False
    else:
        if step % 2 == 0:
            return (f(k1 + 1, k2, w, step + 1) and
                    f(k1, k2 + 1, w, step + 1) and
                    f(k1 + k2, k2, w, step + 1) and
                    f(k1, k2 + k1, w, step + 1))
        else:
            return (f(k1 + 1, k2, w, step + 1) or
                    f(k1, k2 + 1, w, step + 1) or
                    f(k1 + k2, k2, w, step + 1) or
                    f(k1, k2 + k1, w, step + 1))


cnt = 0
for s in range(69, 0, -1):
    if f(9, s, 79, 0):
        print(s)