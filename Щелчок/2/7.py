for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not x or y or not z) and (not x == (not y or z)):
                print(x, z, y)