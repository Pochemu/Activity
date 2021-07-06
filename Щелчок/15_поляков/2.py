for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((not x or z) and (not x or not z or not y)):
                print(y, x, z)