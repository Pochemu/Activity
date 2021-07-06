cnt_j = 0
cnt_e = 0
cnt = 0
file = open('24-s1 (1).txt')
for s in file:
    for i in s:
        if i == 'J':
            cnt_j += 1
        elif i == 'E':
            cnt_e += 1
    if cnt_j > cnt_e:
        cnt += 1
    cnt_e, cnt_j = 0, 0
print(cnt)