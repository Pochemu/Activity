cnt = 0
f = open('Задание_24__6ldp.txt')
for s in f:
    if s.count('X') == s.count('S'):
        cnt += 1
print(cnt)