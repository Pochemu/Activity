for i in range(338472, 338495):
    cnt_del = 0
    for j in range(1, int(i**0.5)):
        if i%j == 0:
            cnt_del += 2
            max_del = j
    if (j+1)**2 == cnt_del:
        cnt_del += 1
    if i % (j+1) == 0:
        cnt_del += 1
    if cnt_del == 4:
        print(i//max_del, i)