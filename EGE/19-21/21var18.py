def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 3 or step == 5):
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2:
        return (f(k1 + 2, k2, w, step + 1) and
                f(k1, k2 + 2, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 2, k2, w, step + 1) or
                f(k1, k2 + 2, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))


ans_1 = []
for s in range(1, 70):
    if f(5, s, 75, 1):
        ans_1.append(s)


def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2:
        return (f(k1 + 2, k2, w, step + 1) and
                f(k1, k2 + 2, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 2, k2, w, step + 1) or
                f(k1, k2 + 2, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))


ans_2 = []
for s in range(1, 70):
    if f(5, s, 75, 1):
        ans_2.append(s)
print(*list(set(ans_1) - set(ans_2)))
