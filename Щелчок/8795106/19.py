def f(k, w, step):
    if k >= w and step == 2:
        return True
    elif k >= w and step == 1 or k < w and step == 2:
        return False
    else:
        return (f(k+1, w, step + 1) or
                f(k*3 - 2, w, step + 1))


for s in range(2, 40):
    if f(s, 40, 0):
        print(s)
        break
