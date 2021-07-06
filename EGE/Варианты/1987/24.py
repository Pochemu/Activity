f = open('24-s1.txt')
cnt = 0
cnt_s = 0
for s in f:
    cnt_s += 1
    if s.count('YZ') > 1:
        cnt += 1
print(cnt)
print(cnt_s)