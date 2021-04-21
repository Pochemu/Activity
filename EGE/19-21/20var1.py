def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 4:
        return True
    else:
        if k1 + k2 < w and step == 4:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2:
        return (f(k1+1, k2, w, step+1) or
                f(k1, k2+1, w, step+1) or
                f(k1*2, k2, w, step+1) or
                f(k1, k2*2, w, step+1))
    else:
        return (f(k1 + 1, k2, w, step + 1) and
                f(k1, k2 + 1, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))

for s in range(1, 51):
    if f(10, s, 61, 1):
        print(s)