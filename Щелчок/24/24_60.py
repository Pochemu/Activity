cnt = 0
f = open('shkolkovo_10.txt')
for s in f:
    if s.count('E') > s.count('A'):
        cnt += 1
print(cnt)