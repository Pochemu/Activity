for i in range(33333, 55556):
    cnt = 0
    sum_num = 0
    for j in str(i):
        sum_num += int(j)
    if sum_num > 35:
        for k in range(2, int(i ** 0.5)):
            if i % k == 0:
                cnt += 2
        if i % (k + 1) == 0:
            cnt += 1
        if cnt == 0:
            print(i, sum_num)
