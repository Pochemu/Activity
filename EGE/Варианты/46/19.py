def F(k1, k2, w, s):
    if k1 + k2 >= w and s == 3:
        return True
    elif (k1 + k2 >= w and (s == 2 or s == 4)) or s == 6:
        return False
    else:
        if s % 2 == 0:
            return (F(k1 + 3, k2, w, s + 1) and
                    F(k1, k2 + 3, w, s + 1) and
                    F(k1 * 2, k2, w, s + 1) and
                    F(k1, k2 * 2, w, s + 1))
        else:
            return (F(k1+3, k2, w, s + 1) or
                    F(k1, k2+3, w, s + 1) or
                    F(k1*2, k2, w, s + 1) or
                    F(k1, k2*2, w, s + 1))


for s in range(1, 70):
    if F(9, s, 79, 1):
        print(s)