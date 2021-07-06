for x in range(2):
    for y in range(2):
        for z in range(2):
            if (x or not y) and not(not z or y):
                print(z, x, y)