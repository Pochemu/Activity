for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(x) or y) and (not (y) or z) and not(w):
                    print(z, w, x, y)