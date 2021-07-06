for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (not x or not y) or ((not x) == (not z))) == 0:
                print(z, y, x)