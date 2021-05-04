def f(k, w, step):
    if k >= w and step == 2:
        return True
    else:
        if k < w and step == 2:
            return False
    return (f(k+1, w, step + 1) or
            f(k+10, w, step + 1))


for s in range(1, 41):
    if f(s, 41, 0):
        print(s)
        break