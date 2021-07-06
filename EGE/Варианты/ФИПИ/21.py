def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 4 or step == 2):
        return True
    elif (k1 + k2 >= w and (step == 3 or step == 1)) or (k1 + k2 < w and step == 4):
        return False
    else:
        if step % 2 == 0:
            return (f(k1 + 1, k2, w, step + 1) and
                    f(k1, k2 + 1, w, step + 1) and
                    f(k1 * 2, k2, w, step + 1) and
                    f(k1, k2 * 2, w, step + 1))
        else:
            return (f(k1 + 1, k2, w, step + 1) or
                    f(k1, k2 + 1, w, step + 1) or
                    f(k1 * 2, k2, w, step + 1) or
                    f(k1, k2 * 2, w, step + 1))


for s in range(1, 94):
    if f(13, s, 107, 0):
        print(s)
        break
