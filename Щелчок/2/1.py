for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x and not y and z) or (not x or y)):
                print(x, y, z)