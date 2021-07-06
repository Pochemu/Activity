cnt = 0
for i in range(1_000_000, 1_300_001):
    n = str(i)
    sum_n = 0
    cnt_3 = 0
    for j in range(7):
        sum_n += int(n[j])
        if int(n[j]) < 3:
            cnt_3 += 1
    if sum_n%10 == 0 and cnt_3 == 7:
        cnt += 1
        if cnt%10 == 0:
            cnt_del = 0
            for k in range(2, int(i**0.5)+1):
                if i%k == 0:
                    cnt_del += 2
                if i == k**2:
                    cnt_del -= 1
            print(i, cnt_del)