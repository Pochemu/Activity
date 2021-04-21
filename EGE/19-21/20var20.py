def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    else:
        if k1 + k2 < w and step == 3:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2 == 0:
        return (f(k1 + 2, k2, w, step + 1) or
                f(k1, k2 + 2, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 2, k2, w, step + 1) and
                f(k1, k2 + 2, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))


for s in range(1, 60):
    if f(5, s, 65, 0):
        print(s)
        break
