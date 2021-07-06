for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not x or ((not z or y) and (z or w))) == 0:
                    print(z, x, y ,w)