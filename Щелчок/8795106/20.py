def f(k, w, step):
    if k >= w and step == 3:
        return True
    elif k >= w and step == 2 or k < w and step == 3:
        return False
    else:
        if step%2:
            return (f(k + 1, w, step + 1) and
                    f((k * 3) - 2, w, step + 1))
        else:
            return (f(k+1, w, step + 1) or
                    f((k*3) - 2, w, step + 1))


for s in range(2, 40):
    if f(s, 40, 0):
        print(s)