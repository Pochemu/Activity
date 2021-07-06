def F(k1, k2, w, step):
    if k1 + k2 >= w and step == 3:
        return True
    elif (k1 + k2 <= w and step == 3) or k1 + k2 >= w:
        return False
    else:
        if step%2 == 0:
            return (F(k1+1, k2, w, step+1) or
                    F(k1, k2+1, w, step + 1) or
                    F(k1*3, k2, w, step + 1) or
                    F(k1, k2*3, w, step + 1))
        else:
            return (F(k1 + 1, k2, w, step + 1) and
                    F(k1, k2 + 1, w, step + 1) and
                    F(k1 * 3, k2, w, step + 1) and
                    F(k1, k2 * 3, w, step + 1))


for s in range(1, 82):
    if F(6, s, 88, 0):
        print(s)