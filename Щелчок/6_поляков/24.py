f = open('24-s1.txt')
cnt = 0
for s in f:
    if s.count('J') > s.count('E'):
        cnt += 1
print(cnt)
f.close()