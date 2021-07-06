cnt = 0
for i in range(129599, 129600):
    cnt_del = 0
    for j in range(2, int(i**0.5)):
        if i%j == 0:
            cnt_del += 2
    print(j)
    if j+1 == i%(j+1):
        cnt_del += 1
    if cnt_del == 4:
        cnt += 1
print(cnt)