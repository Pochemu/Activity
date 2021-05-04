cnt = 0
cnt_max = 0
with open('../../../В процессе/zadanie24_1.txt') as f:
    for s in f:
        for i in s:
            if i == 'A':
                cnt += 1
                cnt_max = max(cnt, cnt_max)
            else:
                cnt = 0
print(cnt_max)