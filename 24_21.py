f = open('../../В процессе/24data/k7a-1.txt')
s = f.readline()
cnt_len, max_len = 0, 0
for i in s:
    if i in 'ABC':
        cnt_len += 1
    else:
        max_len = max(max_len, cnt_len)
        cnt_len = 0
print(max_len)