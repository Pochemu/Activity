for i in range(152_948, 153_015):
    cnt_del = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            cnt_del += 2
        if j**2 == i:
            cnt_del -= 1
    if cnt_del == 0:
        print(i)