def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 3 or step == 5):
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2 == 0:
        return (f(k1 + 3, k2, w, step + 1) or
                f(k1, k2 + 3, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 3, k2, w, step + 1) and
                f(k1, k2 + 3, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))


ans_1 = set()
for s in range(1, 71):
    if f(7, s, 78, 1):
        ans_1.add(s)


def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2 == 0:
        return (f(k1 + 3, k2, w, step + 1) or
                f(k1, k2 + 3, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 3, k2, w, step + 1) and
                f(k1, k2 + 3, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))


ans_2 = set()
for s in range(1, 71):
    if f(7, s, 78, 1):
        ans_2.add(s)
print(*list(ans_1-ans_2))