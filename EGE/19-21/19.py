def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 3 or step == 5):
        return True
    elif (k1 + k2 < w and step == 5) or (k1 + k2 >= w and (step == 4 or step == 2)):
        return False
    if step % 2 == 0:
        return (f(k1+1, k2, w, step+1) or
                f(k1, k2+1, w, step + 1) or
                f(k1*3, k2, w, step + 1) or
                f(k1, k2*3, w, step + 1))
    else:
        return (f(k1 + 1, k2, w, step + 1) and
                f(k1, k2 + 1, w, step + 1) and
                f(k1 * 3, k2, w, step + 1) and
                f(k1, k2 * 3, w, step + 1))


for s in range(1, 73):
    if f(6, s, 79, 1):
        print(s)