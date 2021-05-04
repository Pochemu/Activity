def f(k1, k2, w, step):
    if k1 + k2 >= w and (step == 3 or step == 5):
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2 == 0:
        return (f(k1 + 1, k2, w, step + 1) or
                f(k1, k2 + 1, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 1, k2, w, step + 1) and
                f(k1, k2 + 1, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))


ans_1 = set()
for S in range(1, 31):
    if f(9, S, 40, 1):
        ans_1.add(S)


def f(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    else:
        if k1 + k2 < w and step == 5:
            return False
        elif k1 + k2 >= w:
            return False
    if step % 2 == 0:
        return (f(k1 + 1, k2, w, step + 1) or
                f(k1, k2 + 1, w, step + 1) or
                f(k1 * 2, k2, w, step + 1) or
                f(k1, k2 * 2, w, step + 1))
    else:
        return (f(k1 + 1, k2, w, step + 1) and
                f(k1, k2 + 1, w, step + 1) and
                f(k1 * 2, k2, w, step + 1) and
                f(k1, k2 * 2, w, step + 1))


ans_2 = set()
for S in range(1, 31):
    if f(9, S, 40, 1):
        ans_2.add(S)
print(len(list(ans_1-ans_2)))