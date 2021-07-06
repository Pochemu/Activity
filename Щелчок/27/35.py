cnt = 0
for i in range(50000, 10000, -1):
    cnt_del = 0
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            cnt_del += 2
        if j**2 == i:
            cnt_del -= 1
    if cnt_del > 17:
        cnt += 1
        min_n = i
print(cnt, min_n)