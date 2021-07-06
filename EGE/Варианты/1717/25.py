cnt = 0
for i in range(164700, 164753):
    cnt_del = 0
    x = 0
    for j in range(1, int(i**0.5)):
        if i%j == 0:
            cnt_del += 2
            if cnt_del == 4:
                x = j
    if i % int(i**0.5) == 0:
        cnt_del += 1
    if i % (int(i**0.5) + 1) == 0:
        cnt_del += 1
    if cnt_del == 6:
        cnt += 1
        print(i//x, i)
print(cnt)