for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x and not y) and (not z or not x) and (y == z)):
                print(x, y, z)