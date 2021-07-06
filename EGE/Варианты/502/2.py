x = 0
y = 0
z = 0
w = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not((not x or z) == (y and not w)) or (z and y)) == 0:
                    print(x, y, z, w)