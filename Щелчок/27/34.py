dels = [11, 13, 17, 19]
cnt = 0
for i in range(33000, 22000, -1):
    cnt_del = 0
    for j in range(4):
        if i % dels[j] == 0:
            cnt_del += 1
    if cnt_del == 2:
        cnt += 1
        min_n = i
print(cnt, min_n)