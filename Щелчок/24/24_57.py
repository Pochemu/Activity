f = open('shkolkovo_7.txt')
cnt = 0
cnt_max = 0
for s in f:
    for i in s:
        if i != 'A' and i != 'E':
            cnt += 1
        else:
            cnt_max = max(cnt_max, cnt)
            cnt = 0
print(cnt_max)