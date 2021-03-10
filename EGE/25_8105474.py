cnt_del = 0
cnt_max_del = 0
for i in range(568_023, 569_231):
    for j in range(1, int(i**0.5)):
        if i % j == 0:
            cnt_del += 2
    if i % (j+1) == 0:
        cnt_del += 1
    if i % (i / (j+1)) == 0 and (j+1) != (i / (j+1)):
        cnt_del += 1
    if cnt_del > cnt_max_del:
        cnt_max_del = cnt_del
        answer = i
    cnt_del = 0
print(cnt_max_del, answer)