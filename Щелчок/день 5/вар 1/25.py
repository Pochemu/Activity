for i in range(192_752, 192_818):
    cnt_del = 0
    d = []
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            cnt_del += 2
            d.append(j)
        if i == j**2:
            cnt_del -= 1
    if cnt_del == 4:
        print(d[0], d[1], i//d[1], i//d[0])