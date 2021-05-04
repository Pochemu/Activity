for i in range(1350, 1697):
    last_del = 0
    cnt_del = 0
    for j in range(1, i):
        if i % j == 0:
            cnt_del += 2
            if cnt_del == 4:
                last_del = j
    # if i % (i / i % (j+1)) == 0 and j+1 != i%(j+1):
    #     cnt_del += 1
    if cnt_del == 4:
        print(i**2/last_del, i**2)
cnt = 0
for j in range(1, 1874162):
    if 1874161 % j == 0:
        cnt += 1
        print(j)
print(cnt)