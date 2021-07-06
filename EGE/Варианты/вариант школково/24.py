f = open('24.txt')
cnt = 0
for s in f:
    if s.count('S') == s.count('X'):
        cnt += 1
print(cnt)