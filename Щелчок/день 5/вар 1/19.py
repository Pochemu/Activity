def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 2:
        return True
    elif (k1 + k2 < w and step == 2) or (k1 + k2 >= w and step == 1):
        return False
    else:
        return (f(k1+1, k2, w, step+1) or
                f(k1, k2+1, w, step+1) or
                f(k1*3, k2, w, step+1) or
                f(k1, k2*3, w, step+1))


for s in range(1, 134):
    if f(34, s, 136, 0):
        print(s)
        break
