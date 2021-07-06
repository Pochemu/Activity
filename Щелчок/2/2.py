for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not x or (y and z)) or (z == x)) == 0:
                print(x, y, z)