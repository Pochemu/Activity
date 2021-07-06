def f(k, w, step):
    if k >= w and step == 2:
        return True
    elif (k < w and step == 2) or (k >= w and step == 1):
        return False
    else:
        if step%2 == 0:
            return (f(k+1, w, step+1) and
                    f(k*2, w, step+1))
        else:
            return (f(k + 1, w, step + 1) or
                    f(k * 2, w, step + 1))


for s in range(1, 48):
    if f(s, 48, 0):
        print(s)
        break
