for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if w and (x or (not y)) and (not(w==z)):
                    print(w, z, y, x)