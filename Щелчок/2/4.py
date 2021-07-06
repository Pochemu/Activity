for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((z == y) or (x and y)) == 0:
                print(z, x, y)