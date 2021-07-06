def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    elif (k1 + k2 >= w and step == 2) or (k1 + k2 < w and step == 3):
        return False
    else:
        if step % 2:
            return (f(k1 + 1, k2, w, step + 1) and
                    f(k1, k2 + 1, w, step + 1) and
                    f(k1 + k2, k2, w, step + 1) and
                    f(k1, k2 + k1, w, step + 1))
        else:
            return (f(k1 + 1, k2, w, step + 1) or
                    f(k1, k2 + 1, w, step + 1) or
                    f(k1 + k2, k2, w, step + 1) or
                    f(k1, k2 + k1, w, step + 1))


cnt = 0
for s in range(1, 70):
    if f(9, s, 79, 0):
        print(s)
        cnt += 1
print(cnt)
