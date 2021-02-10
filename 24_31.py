f = open('../../В процессе/24data/k7b-5.txt')
s = f.readline()
cnt, max_len = 0, 0
for i in s:
    if i == 'C' and cnt % 2 == 0 or i == 'A' and cnt % 2 == 1:
        cnt += 1
        max_len = max(max_len, cnt)
    elif i == 'C':
        cnt = 1
    else:
        cnt = 0
print(max_len)