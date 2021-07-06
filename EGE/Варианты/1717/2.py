for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((not x or y) and not z) or w):
                    print(x,w,z, y)