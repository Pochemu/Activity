def f(k, w, step):
    if k >= w and step == 3:
        return True
    else:
        if k < w and step == 3:
            return False
        elif k >= w:
            return False
    if step % 2 == 0:
        return (f(k+1, w, step + 1) or
                f(k+10, w, step + 1))
    else:
        return (f(k + 1, w, step + 1) and
                f(k + 10, w, step + 1))


for s in range(1, 41):
    if f(s, 41, 0):
        print(s)