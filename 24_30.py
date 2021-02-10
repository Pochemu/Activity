f = open('../../В процессе/24data/k7b-4.txt')
s = f.readline()
cnt, max_len = 0, 0
for i in s:
    if (i == 'E' and cnt % 4 == 0 or
            i == 'B' and cnt % 4 == 1 or
            i == 'C' and cnt % 4 == 2 or
            i == 'F' and cnt % 4 == 3):
        cnt += 1
        max_len = max(max_len, cnt)
    elif i == 'E':
        cnt = 1
    else:
        cnt = 0
print(max_len)
