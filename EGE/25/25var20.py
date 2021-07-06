for i in range(4301614, 4301718):
    x = 0
    for j in range(2, int(i**0.5)):
        if i%j == 0:
            x = 1
    if (j+1)**2 == i:
        x = 1
    if x == 0:
        print(i)