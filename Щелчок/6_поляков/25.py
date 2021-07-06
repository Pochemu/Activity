for i in range(338_472, 338_495):
    cnt_del = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            cnt_del += 2
            d = j
        if j**2 == i:
            cnt_del -= 1
    if cnt_del == 2:
        print(i//d, i)