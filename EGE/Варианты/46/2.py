x = 0
y = 0
z = 0
w = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y==w) or (not (z) or w)) and (y == (x or z)):
                    print (x, y, z, w)